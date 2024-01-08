**To install**

1. set up a local directory; use one sub-directory for all data sets, sql scripts, and python files. Or use same sub-directory created in db setup.
```
 $mkdir local_external
 $cd local_external
```
2. map local directory to jupyter/pyspark-notebook python container home.
```
  local_external$ source="$(pwd)" && target='/home/jovyan/work'
```
3. use familiar values for container name, and token values; then create runnable docker container.
```
  local_external$ sudo docker run -itd \ 
    -p 10000:8888 \
    -v $source:$target \
    --name my_pyspark \
    -e GRANT_SUDO=yes --user=root \
    jupyter/pyspark-notebook start-notebook.sh \  
    --NotebookApp.token='a-token' 

```

**To run**

1. open a session in browser.
```
  http://127.0.0.1:10000/lab?token=a-token
```
2. click Terminal button to start a new terminal session; and optionally, add utility programs to running container.
```
  (base) jovyan@072069fadf7b:~$ cat /etc/os-release 

  (base) jovyan@072069fadf7b:~$ sudo apt update
  (base) jovyan@072069fadf7b:~$ sudo apt install vim tree
```
3. to stop and start container.
```
  local_external$ sudo docker container stop my_pyspark
 
  local_external$ sudo docker container start my_pyspark
```
