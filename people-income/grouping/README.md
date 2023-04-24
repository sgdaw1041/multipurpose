**To run db file** 

1. from within db container, exit db session, and cd into work directory to create view object.
``` 
  people_income=> \q
  /home/people-income $ cd grouping
  /home/people-income/grouping $ psql people_income -U user-name -f  create_view_grp.sql

```

2. restart session, and run grouping script
```
  /home/people-income/grouping $ psql people_income -U user-name
  people_income=> \dn
  people_income=> set search_path to grp_query, data_query;
  people_income=> \d+
  people_income=> \d+ grpview_people_income
  people_income=> \i db_grouping.sql  

```
3. stop db container.
``` 
  people_income=> \q
  /home/people-income/grouping $ exit
  /home/people-income/grouping # exit
  $ sudo docker-compose stop
```

**To run python file** 

1. from within running python container, browse to local site and click Terminal button to start a new terminal session.
```
  http://127.0.0.1:10000/lab?token=a-token
```

2. from within sub-directory run file to process data using python pyspark dataframe interactively.
``` 
  ~/work$ cd people-income/grouping
  ~/work/people-income/grouping$ python -i py_grouping.py

```
3. after short run of file, show available session variables and packages.
```
  >>> dir()
```

4. exit the session, close brower, and return to Jupyter terminal.
```
  >>> exit()
  ~/work/people-income/grouping$
```
5. stop python container.
``` 
  $ sudo docker container my_pyspark stop
```


**Contents**

- ```create_view_grp.sql``` create database view object.
- ```db_grouping.sql``` grouping database queries on group-by, rollup, cube, and grouping sets.
- ```py_grouping.py ``` grouping python pyspark code, and/or pyspark SQL, on group-by, rollup, cube, and grouping sets.

