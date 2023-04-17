create schema if not exists grp_query;

set search_path to data_query, grp_query;


-- Create main table for all queries
drop table if exists grp_query.grp_people_income;

create table grp_query.grp_people_income as
select * from people_income;

alter table grp_people_income
  add constraint grp_people_income_pkey PRIMARY KEY (id);

comment on table grp_people_income
  is 'copy of people_income table used for correlation analysis';

-- add integer equivalent of grouped column-pairs (education, education_num)
alter table grp_people_income add column  ed_num integer;

-- monotonically increasing seq acts as integer equivalent of grouped column-pairs
create sequence if not exists grp_query.seq_mono_increasing;

--  initialize sequence
select nextval('seq_mono_increasing');
-- some sequence operations
select currval('seq_mono_increasing');
select setval('seq_mono_increasing', 86);
select nextval('seq_mono_increasing');
select currval('seq_mono_increasing');

-- common table expression to produce values that update table's new column
with cte_grp  as  (
    select education, education_num
    from data_query.people_income
    group by education,  education_num
    order by education_num)
select education, education_num, nextval('seq_mono_increasing') as thenum
  from cte_grp  
  limit 5;

-- use CTE of unique pairs (education, education_num) to update new column 
with cte_grp  as  (
      select education, education_num
      from data_query.people_income
      group by education,  education_num
      order by education_num),
    cte_mono_increase as (
      select education, nextval('seq_mono_increasing') as thenum
      from cte_grp )
update  grp_people_income  gpi
   set ed_num = cte_mono_increase.thenum 
   from cte_mono_increase where gpi.education = cte_mono_increase.education;


-- trivial proof of correlation
select corr( ed_num::double precision, education_num::double precision) as correlation_value 
from grp_people_income;


