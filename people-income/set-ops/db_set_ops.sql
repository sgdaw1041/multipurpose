set search_path to  set_query, data_query;

-- load table of duplicated rows (orig + duplicate row)
insert into notunq_pi 
 select id 
 from people_income 
 where (age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income) 
   in (
     select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income
     from people_income
     group by age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss,    hours_per_week,native_country,income
     having count(*) > 1
   );

select count(*) from notunq_pi;

-- count of all duplicates filtered on duplicated rows list, and sorted on column-values
select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income, count(*) from people_income 
where id in (select id from notunq_pi)
group by age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss,    hours_per_week,native_country,income
order by fnlwgt, age;

-- create table of duplicate rows (without duplicates of duplicates) from original table
insert into dups_people_income (age,workclass,fnlwgt,education,education_num,
marital_status,occupation,relationship,sex,capital_gain,capital_loss,
hours_per_week,native_country,income)
  select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income
  from people_income 
  where id in (select id from notunq_pi)
  group by age,workclass,fnlwgt,education,education_num,   marital_status,occupation,relationship,sex,capital_gain,capital_loss,    hours_per_week,native_country,income;

select count(*) from dups_people_income;

-- create table of unique rows from original table 
insert into unq_people_income (age,workclass,fnlwgt,education,education_num,
marital_status,occupation,relationship,sex,capital_gain,capital_loss,
hours_per_week,native_country,income)
  select distinct age,workclass,fnlwgt,education,education_num,
marital_status,occupation,relationship,sex,capital_gain,capital_loss,
hours_per_week,native_country,income 
  from people_income;

select count(*) from unq_people_income;
    

-- count of sampled tables
select count(*) from set_pi_data1;
select count(*) from set_pi_data2;
select count(*) from set_pi_data3;


-- 2. union together 3 samples, and retain duplicates 
truncate table set_cat;
insert into set_cat(age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income) 
select * from (
   select * from  set_pi_data1
     union all
   select * from  set_pi_data2
     union all
  select * from  set_pi_data3
) unioned_w_dup;

select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income,  count(*) 
from set_cat
group by age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income 
having count(*) > 2;

select count(*) from (
  select  age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income
  from set_cat
  group by  age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income 
  having count(*) > 1
) union_all_ed;

select count(*) from set_cat;


-- 3. union together 3 samples without duplicates
truncate table set_unioned;
insert into set_unioned(age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income) 
select * from (
   select * from  set_pi_data1
     union 
   select * from  set_pi_data2
     union 
  select * from  set_pi_data3
)  unioned;

select count(*) from  set_unioned;

select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income,  count(*) 
from set_unioned
group by age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income 
having count(*) > 1;


-- 4. intersection (without duplicates)
truncate table set_intersect;
insert into set_intersect(age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income)   
 select * from (
   select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income
   from  dups_people_income
     intersect
   select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income
   from  unq_people_income
) data_set_intersect;

-- compare counts of tables involved in intersection operation
select count(*) from set_intersect;
select count(*) from dups_people_income;
select count(*) from unq_people_income;

-- 5. set difference

-- sampled table MINUS original dataset--contains no dups
select *
from  set_pi_data1
   except
select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income
from  unq_people_income;

insert into unq_pi_minus_data1(age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income)   
select * from (
  select age,workclass,fnlwgt,education,education_num, marital_status,occupation,relationship,sex,capital_gain,capital_loss, hours_per_week,native_country,income
  from  unq_people_income
     except
  select *
  from  set_pi_data1
) dataset_minused;


select count(*) from unq_pi_minus_data1;




