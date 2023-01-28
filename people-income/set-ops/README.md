**Setup schema with tables, create 3 sampled datafiles, and load tables** 

1. create 3 sampled datafiles from original dataset using either, within local system,
    
```
    ~./people-income/set-ops$ python3  py_create_setup.py

```

   or, within local system. Note: files must be created by root user

```
    $ sudo docker container exec -it psql14_compose psql people_income -U user-name -f ./home/people-income/set-ops/db_create_setup.sql

```

2. create schema with table
``` 
    people_income=> \q
    /home/people-income $ cd set-ops
    /home/people-income/set-ops $ psql people_income -U user-name -f  create_set_ops.sql
    /home/people-income/set-ops $ psql people_income -U user-name
    people_income=> \dn
    
```


3. import data from csv-file to respective tables 
```
    people_income=> set search_path to  set_query, data_query;
    people_income=> \d
    people_income=> \copy  set_pi_data1("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","sex","capital_gain","capital_loss","hours_per_week","native_country","income") from './set_income_data1.csv' delimiter ',' csv header

    people_income=> \copy  set_pi_data2("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","sex","capital_gain","capital_loss","hours_per_week","native_country","income") from './set_income_data2.csv' delimiter ',' csv header

    people_income=> \copy  set_pi_data3("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","sex","capital_gain","capital_loss","hours_per_week","native_country","income") from './set_income_data3.csv' delimiter ',' csv header

``` 

4. run set-ops script to load tables and perform analysis

``` 
    people_income=> \i db_set_ops.sql
    
```

**Contents** 

- ```create_set_ops.sql``` create schema and tables.
- ```db_create_setup.sql``` create 3 csv-file samples with non-duplicate rows from main table.
- ```py_create_setup.py``` create 3 csv-file samples with no replacement from main dataset.
- ```db_set_ops.sql``` set operation database queries.
- ```py_set_ops.py ```  set operation python code.

