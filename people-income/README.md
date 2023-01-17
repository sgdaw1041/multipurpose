# Table of Contents
1. [Setup] (#setup)
2. [Basics] (#basics()
3. [Set] (#set)



## Setup
 Setup user, schema with table, and utility function** 

1. In a running db (here, a docker container) create user
``` 
    $ sudo docker container exec -it psql14_compose sh
    / # cd /home/people-income
    /home/people-income # su postgres -
    /home/people-income $ psql  postgres  -U postgres -f create_user.sql 
```

2. create schema with table, and utility function
``` 
    /home/people-income $ psql people_income -U user-name -f  create_people_income_schema.sql
    /home/people-income $ psql people_income -U user-name
    people_income=> \dn
    people_income=> \df
```

3. import data from csv-file
```
    people_income=> set search_path to data_query;
    people_income=> \d  people_income
    people_income=> \copy  people_income("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","sex","capital_gain","capital_loss","hours_per_week","native_country","income") from 'test_income_data1.csv' delimiter ',' csv header
``` 
4. check result
```
    people_income=> \x
    people_income=> select *  from people_income limit 2;
    people_income=> \x
    people_income=> select count(*) from people_income;
```

## Basics
. db_basics.sql contains basic queries
. py_basics.py  contains basic python
