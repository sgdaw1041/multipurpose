set search_path to  set_query;


\copy  set_pi_data1("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","sex","capital_gain","capital_loss","hours_per_week","native_country","income") from './set_income_data1.csv' delimiter ',' csv header

\copy  set_pi_data2("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","sex","capital_gain","capital_loss","hours_per_week","native_country","income") from './set_income_data2.csv' delimiter ',' csv header

\copy  set_pi_data3("age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","sex","capital_gain","capital_loss","hours_per_week","native_country","income") from './set_income_data3.csv' delimiter ',' csv header

