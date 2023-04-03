**To run db file** 


1. from within container, exit db session, and cd into work directory to run file
``` 
    people_income=> \q
    /home/people-income $ cd basics
    /home/people-income/basics $ psql people_income -U user-name -f  db_basics.sql
```

2. restart session 
    
```
    /home/people-income/basics $ psql people_income -U user-name
    people_income=> \dn
    people_income=> set search_path to public, data_query;
    people_income=> \d+
```

**To run python file** 

1. from within running python container, browse to local site and click Terminal button to start a new terminal session.
```
  http://127.0.0.1:10000/lab?token=a-token
```

2. from within sub-directory run file to process data using python pyspark dataframe interactively.
``` 
  ~/work$ cd people-income/basics
  ~/work/people-income/basics$ python -i py_basics.py

```
3. after short run of file, show available session variables and packages.
```
  >>> dir()
```

4. exit the session, close brower, and return to Jupyter terminal.
```
  >>> exit()
  ~/work/people-income/basics$
```
5. stop python container.
``` 
  $ sudo docker container my_pyspark stop
```


**Contents**

- ```db_basics.sql``` basic database queries.
- ```py_basics.py ``` basic python pandas code.


