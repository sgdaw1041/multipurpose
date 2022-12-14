drop db if exists people_income;

drop role if exists user-name;

create ROLE user-name PASSWORD 'got-a-password-here' CREATEDB  INHERIT LOGIN;


CREATE DATABASE people_income ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8' TEMPLATE template0 OWNER user-name;


