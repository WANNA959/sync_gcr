# coding:utf-8
import subprocess
import os


def get_filename():
    with open("images.txt", "r") as f:
        lines = f.read().split('\n')
        # print(lines)
        return lines


username = os.environ.get('DOCKER_USERNAME', '')
password = os.environ.get('DOCKER_PASSWORD', '')
namespace = os.environ.get('DOCKER_NS', '')


def pull_image():

    name_list = get_filename()
    for name in name_list:
        if 'sha256' in name:
            print(name)
            sha256_name = name.split("@")
            new_name = sha256_name[0].split("/")[-1]
            tag = sha256_name[-1].split(":")[-1][0:6]
            image = "registry.cn-hangzhou.aliyuncs.com/{0}/{1}:{2}".format(namespace, new_name, tag)
            subprocess.call("docker pull {}".format(name), shell=True)
            subprocess.run(["docker", "tag", name, image])
            subprocess.call(
                "docker login -u {0} -p {1} registry.cn-hangzhou.aliyuncs.com".format(username, password), shell=True)
            subprocess.call("docker push {}".format(image), shell=True)
        else:
            new_name = "registry.cn-hangzhou.aliyuncs.com" + "/" + namespace + "/" + name.split("/")[-1]
            subprocess.call("docker pull {}".format(name), shell=True)
            subprocess.run(["docker", "tag", name, new_name])
            subprocess.call(
                "docker login -u {0} -p {1} registry.cn-hangzhou.aliyuncs.com".format(username, password), shell=True)
            subprocess.call("docker push {}".format(new_name), shell=True)


if __name__ == "__main__":
    pull_image()
