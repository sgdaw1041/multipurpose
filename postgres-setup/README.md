
1. set up a local sub-directory for all data sets, sql-scripts, and python files.
```
  $ mkdir local_external
```
2. copy docker-compose.yml beside new sub-directory, not inside sub-directory, and run docker-compose to create a postgresql 14 container.
```   
  $ sudo docker-compose up -d
  $ sudo docker-compose stop
```
3. mount container 
```
  $ sudo docker-compose start
  $ sudo docker container exec -it psql14_compose sh
```

4. cd into mapped directory at container home.
```
  / # cd /home/people-income/
```

5. switch to postgres user 
```
  /home/people-income # su postgres -
```