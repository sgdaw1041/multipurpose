# Table of Contents
1. [Setup](#setup)
2. [Basics](#basics)
3. [Set-ops](#set-ops)
4. [Group-correlation](#group-correlation)
4. [Grouping](#grouping)



## Setup
 Setup database user, schema with table, and utility function 

1. In a running db (here, a docker container) create user
``` 
    $ sudo docker container exec -it psql14_compose sh
    / # cd /home/people-income
    /home/people-income # su postgres -
    /home/people-income $ psql  postgres  -U postgres -f create_user.sql 
```

2. create schema, table, and utility function. And, populate table
``` 
    /home/people-income $ psql people_income -U user-name -f  create_people_income_schema.sql
    /home/people-income $ psql people_income -U user-name -f  db_populate.sql
```

3. check result
```
    /home/people-income $ psql people_income -U user-name
    people_income=> \dn
    people_income=> \df
    people_income=> set search_path to public, data_query;
    people_income=> \d
    people_income=> \x
    people_income=> select *  from people_income limit 2;
    people_income=> \x
    people_income=> select count(*) from people_income;
```

4. exit postgres container
```
    people_income=> \q
    /home/people-income $ exit
    /home/people-income # exit

```

## Basics

- ```db_basics.sql``` basic database queries.
- ```py_basics.py ``` basic python pandas code.


## Set-ops

##### Identify duplicate rows and mitigate their effect during Set operations. And, run various Set operations including union all, union, intersection, and Set difference.

- ```create_set_ops.sql``` create schema and tables.
- ```db_create_samples.sql``` create 3 csv-file samples with no duplicate rows per sample from main table.
- ```py_create_samples.py``` create 3 csv-file samples with no replacement from main dataset.
- ```db_populate_samples.sql``` load 3 csv-files sampled from main table; load either python or db generated files.
- ```db_set_ops.sql``` set operation database queries.
- ```py_set_ops.py ```  set operation python pandas code.

## Group-correlation

##### Create integer equivalent of text field, and prove validity by correlation with another integer field in same object
- ```db_grp-corr.sql``` database sql correlation on integer field based on grouped values and ordering field in same table.
- ```py_grp-corr.py ``` pandas code correlation on integer field based on grouped values and ordering field in same dataframe.

## Grouping

##### Create groupings using group-by, rollup, cube, composite columns on multi-column groups, and grouping sets. And use grouping() functions to flag grouped rows.
- ```create_view_grp.sql``` create database view object.
- ```db_grouping.sql``` grouping database queries on group-by, rollup, cube, and grouping sets.
- ```py_grouping.py ``` grouping python pyspark code, and/or pyspark SQL, on group-by, rollup, cube, and grouping sets.
