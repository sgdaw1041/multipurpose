import numpy as np
import pandas as pd


df = pd.read_csv('../test_income_data1.csv')

# show shape and describe columns
print(df.shape)
df.info()

# ####  part 1 search for duplicate rows, and create dataframe of unique rows ####

# get a boolean series on duplicated rows (orig + duplicate row)
df_bool_notunq    = df.duplicated(keep=False)

print ('\nall duplicates filtered on bool list, and sorted on column-values')
print( df[ df_bool_notunq.values.tolist() ].sort_values(by = ['fnlwgt', 'age']) )

# list of all columns in dataframe
df_cols = df.columns.values.tolist()
print ('\n# dataframe of dups with count of duplicate rows')
print (df.groupby(df_cols).size().sort_values(ascending=False).loc[lambda x: x > 1].reset_index(name='count-is'))

print ('\n## -- dataframe of duplicate rows (without duplicates of duplicates) from original table ')
df_dups = df[ df_bool_notunq.values.tolist() ].drop_duplicates(keep='first', ignore_index=True)

print(df_dups)

# original dataset with duplicated rows removed
d_unq = df.drop_duplicates(keep='first', ignore_index=True)

# load 3 sampled dataframes--approx 10% each for set operations
df_1 = pd.read_csv('./set_income_data1.csv')
df_2 = pd.read_csv('./set_income_data2.csv')
df_3 = pd.read_csv('./set_income_data3.csv')


###################################################
####  part 2 union-all (retain all duplicates)  ###

print('\n  # union all operation')
df_cat = pd.concat([df_1,df_2,df_3], axis=0)

print(df_cat.shape)

print ('\n# dataframe: count of duplicate rows > 2')
print(df_cat.groupby(df_cols).size().sort_values(ascending=False).loc[lambda x: x > 2].reset_index(name='count-is'))

df_cat_grouped = df_cat.groupby(df_cols).size().sort_values(ascending=False).loc[lambda x: x> 1 ].reset_index(name='count-is')

print('\n# count of duplicates across 3 sampled datasets')
print(df_cat_grouped.shape)

###################################################
#  part 3:  union (drop duplicates)  

print('\n dataframe of unioned sampled datasets')
df_unioned   = pd.concat([df_1,df_2,df_3], axis=0).drop_duplicates()

print(df_unioned.shape)

# for comparison with union-all ops, make boolean series of dups
# get a boolean series (orig + duplicated row)
df_dup_ed    = df_unioned.duplicated(keep=False)

#  Proof: successful deletion of duplicate rows
# 1. filter using a bool array -- for a Series via .values
df_unioned[df_dup_ed.values].size

# 2. or...
len(df_unioned[df_dup_ed.values])
# count is 0

###################################################
###  part 4 intersection - remove duplicates ##
  
# dataframe of all duplicate rows from original dataset (same as df_dups)
df.groupby(df_cols).filter(lambda x : len(x) > 1).drop_duplicates()

print('\n# set intersection of original dataset with duplicated rows removed and dataframe of duplicate rows from original table' )
df_intersect = pd.merge(d_unq, df_dups, how='inner', on=df_cols)

print(df_intersect)

###################################################
  ####  part 5 difference  ####

print('\n# dataframe of original dataset--contains no dups')
print(d_unq.shape)
print('\n# dataframe dataset approx 10% of original dataset--contains no dups')
print(df_1.shape)


# create list-of-tuples, as a set, to enable set-difference operator
#  https://stackoverflow.com/questions/18180763/set-difference-for-pandas
dsd_1   = set(map(tuple, df_1.values))
dsd_unq = set(map(tuple, d_unq.values))

# take set differences 
dsd_1_minus_dsd_unq = pd.DataFrame(list(dsd_1.difference(dsd_unq)), columns=df_cols)
dsd_unq_minus_dsd_1 = pd.DataFrame(list(dsd_unq.difference(dsd_1)), columns=df_cols)

dsd_1_minus_dsd_unq['age'].count()
# 0
print ('\n# sizeof original dataset with duplicated rows removed  MINUS sizeof a sampled dataset')
print(dsd_unq_minus_dsd_1['age'].count())
# sizeof(d_unq) - sizeof(df_1)


