set search_path to public, data_query;

-- show shape and describe columns
select column_name, data_type, is_identity as "identity" ,numeric_precision as "precision", is_nullable as "nullable"
from information_schema.columns
where table_schema = 'data_query' and table_name = 'people_income';


-- https://stackoverflow.com/questions/53087945/how-can-i-get-a-count-of-all-the-columns-in-a-table-using-postgresql
--   execute function dynamically
select f.column_name, f.count from get_count('data_query', 'people_income') as f(column_name, count) ;

-- Make a list of all variables with classes
select column_name, data_type  from information_schema.columns
where data_type like '%character varying%' and table_schema= 'data_query' and table_name= 'people_income';

--          *** simple queries ***
-- select 5 unique records
select distinct native_country from people_income limit 5;

-- sort list as lexicographic 5 unique records
select distinct native_country from people_income
order by native_country asc limit 5;

-- 5 records with simple-predicate
select * from people_income where native_country = 'Cambodia' limit 5;

-- select 5 records of named columns with simple-predicate
select age,workclass,education,education_num from people_income
where native_country = 'Cambodia' limit 5;

--          *** group-by ***
-- # object with statistics on 'age' within grouped 'workclass
select f.column_name, f._count, f._mean, f._stddev, f._min, f._pct25, f._pct50, f._pct75,  f._max
from get_grpstats('data_query', 'people_income', 'workclass', 'age')
   as f(column_name, _count, _mean, _stddev, _min, _pct25, _pct50, _pct75, _max) ;

-- # object with statistics on 'hours_per_week' within grouped 'workclass
select f.column_name, f._count, f._mean, f._stddev, f._min, f._pct25, f._pct50, f._pct75,  f._max
from get_grpstats('data_query', 'people_income', 'workclass', 'hours_per_week')
   as f(column_name, _count, _mean, _stddev, _min, _pct25, _pct50, _pct75, _max) ;

-- # object with statistics on 'age' within grouped 'education'
select f.column_name, f._count, f._mean, f._stddev, f._min, f._pct25, f._pct50, f._pct75,  f._max
from get_grpstats('data_query', 'people_income', 'education', 'age')
   as f(column_name, _count, _mean, _stddev, _min, _pct25, _pct50, _pct75, _max) ;


select workclass, count(*) as "count-is" from people_income
group by workclass;

-- group-by on two fields with counts
select sex, workclass, count(*) as "count-is" from people_income
group by sex, workclass order by sex;

-- group-by sorted by frequency of classes having count specified
select workclass, count(*) as "count-is" from people_income
group by workclass having count(*) < 100 order by count(*) desc;

-- with simple-predicate, group-by on multiple columns having count specified and sorted by a selection
select education,education_num, occupation, count(*)
from people_income where income like '%>50K%'
group by education,education_num, occupation
having count(*) > 30
order by education_num desc;


-- subquery using max()
-- count(*) with predicate where  max(capital_loss)
select count(*)  from people_income
where capital_loss in  (select max(capital_loss) from people_income);

-- select workclass, sex, age   with predicate where  max(capital_loss)
select workclass, sex, age  from people_income
where capital_loss in  (select max(capital_loss) from people_income);



