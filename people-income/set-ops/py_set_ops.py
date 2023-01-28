import numpy as np
import pandas as pd
from tabulate import tabulate

df = pd.read_csv('../test_income_data1.csv')

# show shape and describe columns
print(df.shape)
df.info()

# ####  part 1 search for duplicate rows, and create dataframe of unique rows ####

# get a boolean series on duplicated rows (orig + duplicate row)
df_bool_notunq    = df.duplicated(keep=False)

# all duplicates filtered on bool list, and sorted on column-values
df[ df_bool_notunq.values.tolist() ].sort_values(by = ['fnlwgt', 'age'])

# list of all columns in dataframe
df_cols = df.columns.values.tolist()
# dataframe of dups with count of duplicate rows
df.groupby(df_cols).size().sort_values(ascending=False).loc[lambda x: x > 1].reset_index(name='count-is')

## -- dataframe of duplicate rows (without duplicates of duplicates) from original table 
df_dups = df[ df_bool_notunq.values.tolist() ].drop_duplicates(keep='first', ignore_index=True)

# original dataset with duplicated rows removed
d_unq = df.drop_duplicates(keep='first', ignore_index=True)

# load 3 sampled dataframes--approx 10% each for set operations
df_1 = pd.read_csv('./set_income_data1.csv')
df_2 = pd.read_csv('./set_income_data2.csv')
df_3 = pd.read_csv('./set_income_data3.csv')


###################################################
####  part 2 union-all (retain all duplicates)  ###

  # union all operation
df_cat = pd.concat([df_1,df_2,df_3], axis=0)

print(df_cat.shape)

# dataframe: count of duplicate fnlwgt (NOTE: df_cols uses all columns)
df_cat.groupby(df_cols).size().sort_values(ascending=False).loc[lambda x: x > 2].reset_index(name='count-is')

# size of union-all dataframe
print(df_cat_grouped.shape)


print(tabulate(df_cat_grouped, headers = 'keys', tablefmt = 'git'))

###################################################
#  part 3:  union (drop duplicates)  

# create dataframe of non-duplicates
df_unioned   = pd.concat([df_1,df_2,df_3], axis=0).drop_duplicates()

print(df_unioned.shape)

# for comparison with union-all ops, make boolean series of dups
# get a boolean series (orig + duplicated row)
df_dup_ed    = df_unioned.duplicated(keep=False)

#  Proof: successful deletion of duplicate rows
# 1. filter using a bool array -- for a Series via .values
print(df_unioned[df_dup_ed.values].size)

# 2. or...
len(df_unioned[df_dup_ed.values])
# count is 0

###################################################
###  part 4 intersection - remove duplicates ##
  
# dataframe of all duplicate rows from original dataset (same as df_dups)
df.groupby(df_cols).filter(lambda x : len(x) > 1).drop_duplicates()

# set intersection of above dataframe with original dataset with duplicated rows removed
df_intersect = pd.merge(d_unq, df_dups, how='inner', on=df_cols)

###################################################
  ####  part 5 difference  ####

# dataframe of original dataset--contains no dups
d_unq.shape
# dataframe dataset approx 10% of original dataset--contains no duplicate row(s)
df_1.shape


# create list-of-tuples, as a set, to enable set-difference operator
#  https://stackoverflow.com/questions/18180763/set-difference-for-pandas
dsd_1   = set(map(tuple, df_1.values))
dsd_unq = set(map(tuple, d_unq.values))

# take set differences 
dsd_1_minus_dsd_unq = pd.DataFrame(list(dsd_1.difference(dsd_unq)), columns=df_cols)
dsd_unq_minus_dsd_1 = pd.DataFrame(list(dsd_unq.difference(dsd_1)), columns=df_cols)

dsd_1_minus_dsd_unq['age'].count()
# 0
dsd_unq_minus_dsd_1['age'].count()
# sizeof(d_unq) - sizeof(df_1)


