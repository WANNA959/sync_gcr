# sync_gcr

> 作用: 同步k8s集群所需镜像

- 列出集群所有镜像

```shell
kubectl get pods --all-namespaces -o jsonpath="{..image}" |\
tr -s '[[:space:]]' '\n' |\
sort |\
uniq 
```

- 复制到images.txt
- 提交即可触发github action 同步images.txt的镜像到本人的dockerhub
- ci run完通过 python3 load_image.py 把镜像下载到本地,并重新tag
