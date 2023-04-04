# coding:utf-8
import subprocess
import os


def get_filename():
    with open("images.txt", "r") as f:
        lines = f.read().split('\n')
        # print(lines)
        return lines

# def rename():
#     name_list= get_filename()
#     for name in name_list:
#         new_name = "wannazjx/" + name.split("/")[-1]
#         print(new_name)


def pull_image():
    password = os.environ.get('DOCKER_PASSWORD')
    name_list = get_filename()
    for name in name_list:
        if 'sha256' in name:
            print(name)
            sha256_name = name.split("@")
            new_name = sha256_name[0].split("/")[-1]
            tag = sha256_name[-1].split(":")[-1][0:6]
            image = "wannazjx/" + new_name + ":" + tag
            cmd = "docker tag {0}   {1}".format(name, image)
            subprocess.call("docker pull {}".format(name), shell=True)
            subprocess.run(["docker", "tag", name, image])
            subprocess.call("docker login -u wannazjx -p " +
                            password, shell=True)
            subprocess.call("docker push {}".format(image), shell=True)
        else:
            new_name = "wannazjx/" + name.split("/")[-1]
            cmd = "docker tag {0}   {1}".format(name, new_name)
            subprocess.call("docker pull {}".format(name), shell=True)
            subprocess.run(["docker", "tag", name, new_name])
            subprocess.call("docker login -u wannazjx -p " +
                            password, shell=True)
            subprocess.call("docker push {}".format(new_name), shell=True)


if __name__ == "__main__":
    pull_image()
