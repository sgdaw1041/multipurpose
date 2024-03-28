**To install**

1. set up a local directory; use one sub-directory for all data sets, sql scripts, and python files. Or use same sub-directory created in python setup.
```
  $ mkdir local_external
```

2. map local directory to container
```
  $ source="$(pwd)/local_external" && target='/home'
```

3. create a new running container
```
  $ sudo docker run -it  --mount type=bind,source=$source,target=$target  --name psql15_alpine -e POSTGRES_USER=postgres  -e POSTGRES_PASSWORD=postgres  -p 5435:5432  -d postgres:15-alpine
```

4. stop docker container
```
  $ sudo docker container stop psql15_alpine
```


**To run**


1. start database container, and mount database container 
```
  $ sudo docker container start psql15_alpine

  $ sudo docker container exec -it psql15_alpine sh
```

2. cd into mapped directory at container home.
```
  / # cd /home
```

3. switch to postgres user 
```
  /home # su postgres -
```