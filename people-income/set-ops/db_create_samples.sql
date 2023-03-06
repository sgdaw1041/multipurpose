set search_path to data_query;

-- create 3 sampled data-tables, without duplicate rows per sample.  NOTE: using random sampling without replacement

-- https://stackoverflow.com/questions/8674718/best-way-to-select-random-rows-postgresql


\copy (select  age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income   from data_query.people_income  group by age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income   order by random( ) limit 3250) to '/home/people-income/set-ops/set_income_data1.csv' with csv header;


\copy (select  age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income   from data_query.people_income  group by age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income   order by random( ) limit 3250) to '/home/people-income/set-ops/set_income_data2.csv' with csv header;

\copy (select  age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income   from data_query.people_income  group by age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income   order by random( ) limit 3250) to '/home/people-income/set-ops/set_income_data3.csv' with csv header;

