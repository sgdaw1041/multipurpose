
1. set up a local directory, directory containing docker-compose.yml file, for all data sets and sql-scripts and map it
```
$ mkdir local_external
$ source="$(pwd)/local_external" && target='/home'
```
2. run docker-compose to create a postgresql 14 container
```   
$ sudo docker-compose up -d
$ sudo docker-compose stop
```
3. mount container 
```
$ sudo docker-compose start
$ sudo docker container exec -it psql14_compose sh
```

4. cd into mapped directory at container /home

5. switch to postgres user
   ```
    su postgres -
   ```
