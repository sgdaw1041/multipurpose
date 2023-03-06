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
    people_income=> \d

```

**Contents**

- ```db_basics.sql``` basic database queries.
- ```py_basics.py ``` basic python code.


