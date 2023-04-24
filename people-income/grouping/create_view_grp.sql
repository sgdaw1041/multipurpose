create schema if not exists grp_query;


-- prepare subset of records for table
select native_country, count(*) 
from data_query.people_income 
where native_country in ('Germany', 'Canada', 'England', 'Italy', 'Japan', 'France','Scotland', 'Holand-Netherlands', 'Ireland', 'Taiwan')
  group by native_country
order by count(*) desc;


-- Create main view on table for all queries
create or replace view grp_query.grpview_people_income as
select * from data_query.people_income
where native_country in ('Germany', 'Canada', 'England', 'Italy', 'Japan', 'France','Scotland', 'Holand-Netherlands', 'Ireland', 'Taiwan');

comment on view  grp_query.grpview_people_income  is 'select records from  people_income table limited to 10 countries';

