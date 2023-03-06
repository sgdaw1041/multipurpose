set search_path to data_query;

\copy  people_income("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","sex","capital_gain","capital_loss","hours_per_week","native_country","income")   from 'test_income_data1.csv' delimiter ',' csv header
