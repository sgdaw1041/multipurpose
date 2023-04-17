**To run db file** 


1. from within container, exit db session, and cd into work directory to run file
``` 
    people_income=> \q
    /home/people-income $ cd group-correlation
    /home/people-income/group-correlation $ psql people_income -U user-name -f  db_grp_corr.sql
```

2. restart session 
    
```
    /home/people-income/group-correlation $ psql people_income -U user-name
    people_income=> \dn
    people_income=> set search_path to data_query, grp_query;
    people_income=> \d+
```

**To run python file** 

1. from within running python container, browse to local site and click Terminal button to start a new terminal session.
```
  http://127.0.0.1:10000/lab?token=a-token
```

2. from within sub-directory run file to process data using python pyspark dataframe interactively.
``` 
  ~/work$ cd people-income/group-correlation
  ~/work/people-income/group-correlation$ python -i py_grp_corr.py

```
3. after short run of file, show available session variables and packages.
```
  >>> dir()
```

4. exit the session, close brower, and return to Jupyter terminal.
```
  >>> exit()
  ~/work/people-income/group-correlation$
```
5. stop python container.
``` 
  $ sudo docker container my_pyspark stop
```


**Contents**

- ```db_grp_corr.sql``` database sql correlation on integer field from grouped fields and ordering field in dataframe.
- ```py_grp_corr.py ``` pandas code correlation on integer field from grouped fields and ordering field in dataframe.



