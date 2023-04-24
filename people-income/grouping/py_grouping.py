from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('grouping') \
    .getOrCreate()

df= spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("../test_income_data1.csv")

df.coalesce(1)

df.printSchema()

# show 1st record
df.show(1, False, True)

# create list of select countries
countries = ['Germany', 'Canada', 'England', 'Italy', 'Japan', 'France','Scotland', 'Holand-Netherlands', 'Ireland', 'Taiwan']

# create dataframe  select countries
df_view = df.where(F.col("native_country").isin(countries))

print('record count of view dataframe is {}, followed by example record'.format(df_view.count() ))
df_view.show(1, False, True)

# use SQL: (1) show pyspark code and SQL have same explain plan, (2) use SQL way when pyspark code unknown
df_view.createTempView('view_pi')

# compare pyspark explain plan using  spark way and SQL way
df_view.groupBy("sex", "education")\
  .agg( F.count("*").alias("count_is")) \
  .sort( F.col("sex").asc(), F.col("education") ).explain()

qry1 = "select sex, education, count(*) as count_is \
        from view_pi \
        where capital_gain <> 0 \
        group by  sex,  education \
        order by  sex asc,  education"

spark.sql(qry1).explain()

### rollup 
##-- grouping() flag shows 0 for detail and 1 for group subtotal
## use rollup with composite columns and treat columns as a single unit when determining the necessary groupings
## grouping on {(SNE), (SN), (S), ()}
df_view \
    .where(F.col("capital_gain")  != 0) \
    .rollup(F.col('sex'),F.col('native_country'),F.col('education')) \
    .agg( (F.concat(F.grouping('sex'),F.grouping('native_country'),F.grouping('education') )) \
                   .alias('grp_flag'),F.count("*").alias("count_is") ) \
    .orderBy("sex", "native_country", "education") \
    .show(60)

# 
## use rollup with composite columns and treat columns as a single unit when determining the necessary groupings
## grouping on {(SNE), (SN), ()}, eliminates grouping on {(S)}, i.e. is_grpd of 011

### need pyspark code for spark way for rollup using composite column; here, use SQL way # 
qry2 = "select CONCAT(GROUPING(sex), GROUPING(native_country), GROUPING(education)) as grp_flag \
                           ,sex, native_country, education, count(*) as count_is \
        from view_pi \
        where capital_gain <> 0 \
        group by  rollup ( (sex, native_country), education ) \
        order by  sex, native_country, education"

spark.sql(qry2).show(60)

# grouping_id() to show level of grouping
df_view \
    .where(F.col("capital_gain")  != 0) \
    .rollup(F.col('sex'),F.col('native_country'),F.col('education')) \
    .agg( F.grouping_id(),F.count("*").alias("count_is") ) \
    .orderBy("sex", "native_country", "education") \
    .show(60)


# cube shows all possible combination of grouping
df_view \
    .where(F.col("capital_gain")  != 0) \
    .cube(F.col('sex'),F.col('native_country'),F.col('education')) \
    .agg( F.grouping_id(), (F.concat(F.grouping('sex'),F.grouping('native_country'),F.grouping('education') )) \
                   .alias('grp_flag'),F.count("*").alias("count_is") ) \
    .orderBy("sex", "native_country", "education") \
    .show(70)

# cube with composite columns
# -- grouping on {(SNE), (SN), (E), ()}, eliminates grouping on {(SE), (S), (NE), (N)}
### need pyspark code for spark way for cube using composite column; here, use SQL way #  #
qry3 = "select CONCAT(GROUPING(sex), GROUPING(native_country), GROUPING(education)) as grp_flag \
                          ,GROUPING_ID() as grpid_flag \
                          ,sex, native_country, education, count(*) as count_is \
        from view_pi \
        where capital_gain <> 0 \
        group by  cube ( (sex, native_country), education ) \
        order by  sex, native_country, education"

spark.sql(qry3).show(70)

# -- using grouping sets
#--  create a UNION ALL of group by (sex, native_country) with group by (education)
### need pyspark code for spark way for grouping sets; here, use SQL way #  #
qry4 = "select CONCAT(GROUPING(sex), GROUPING(native_country), GROUPING(education)) as grp_flag \
                           ,sex, native_country, education, count(*) as count_is \
        from view_pi \
        where capital_gain <> 0 \
        group by  GROUPING SETS ( (sex, native_country), education ) \
        order by  sex, native_country, education"

spark.sql(qry4).show(70)
