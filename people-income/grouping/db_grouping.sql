set search_path to  grp_query;

-- group by with count on two columns
select sex, education, count(*)
from grpview_people_income
group by  sex, education
order by sex, education;


-- same group by with rollup adds group subtotals
select sex, education, count(*)
from grpview_people_income  
group by  rollup (sex,  education)
order by  sex, education;

-- grouping shows 0 for detail and 1 for group subtotal
--  group by on 3 columns, here limit using predicate
select  GROUPING(sex)::varchar(1) || GROUPING(native_country)::varchar(1) || GROUPING(education)::varchar(1) as grp_flag,
        sex, native_country, education, count(*)
from grpview_people_income 
  where capital_gain <> 0
group by  rollup (sex, native_country, education)
order by  sex, native_country, education;

-- source https://oracle-base.com/articles/misc/rollup-cube-grouping-functions-and-grouping-sets#composite_columns
-- use rollup with composite columns and treat columns as a single unit when determining the necessary groupings
-- grouping on {(SNE), (SN), ()}, eliminates grouping on {(S)}, i.e. grp_flag of 011
select sex, native_country, education, count(*), 
       GROUPING(sex)::varchar(1) || GROUPING(native_country)::varchar(1) || GROUPING(education)::varchar(1) as grp_flag
from grpview_people_income
  where (capital_gain <> 0)
group by  rollup ((sex, native_country), education)
order by  sex, native_country, education;


-- postgresql doesn't provide GROUPING_ID() function, use lpad( concat(vals),64,'0')::bit(64)::bigint transformation
--  https://stackoverflow.com/questions/1503226/function-in-postgres-to-convert-a-varchar-to-a-big-integer#1503276
select  lpad(CONCAT(GROUPING(sex)::varchar(1),GROUPING(native_country)::varchar(1),GROUPING(education)::varchar(1)),64,'0')::bit(64)::bigint as grpid_level,
        sex, native_country, education, count(*)
from grpview_people_income 
  where capital_gain <> 0
group by  rollup (sex, native_country, education)
order by  sex, native_country, education;


-- use cube to calculate all combination of groups, and add composite columns to create
select  CONCAT(GROUPING(sex)::varchar(1),GROUPING(native_country)::varchar(1),GROUPING(education)::varchar(1)) as grp_flag,
        sex, native_country, education, count(*)
from grpview_people_income 
  where capital_gain <> 0
group by  cube (sex, native_country, education)
order by  sex, native_country, education;


-- grouping on {(SNE), (SN), (E), ()}, eliminates grouping on {(SE), (S), (NE), (N)}
select sex, native_country, education, count(*), 
       CONCAT(GROUPING(sex)::varchar(1),GROUPING(native_country)::varchar(1),GROUPING(education)::varchar(1)) as grp_flag
from grpview_people_income
  where (capital_gain <> 0)
group by  cube ((sex, native_country), education)
order by  sex, native_country, education;


-- using grouping sets
--  create a UNION ALL of group by (sex, native_country) with group by (education)
select sex, native_country, education, count(*), 
       CONCAT(GROUPING(sex)::varchar(1),GROUPING(native_country)::varchar(1),GROUPING(education)::varchar(1)) as grp_flag
from grpview_people_income
  where (capital_gain <> 0)
group by  grouping sets ((sex, native_country), education)
order by  sex, native_country, education;



