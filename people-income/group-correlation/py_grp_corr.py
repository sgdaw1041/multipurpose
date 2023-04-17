import numpy as np
import pandas as pd

df = pd.read_csv('../test_income_data1.csv')

# show shape and describe columns
df.shape
df.info()

# create a groupby dataframe
df_grp = df.groupby(['education','education_num']).size().reset_index(name='count-is')

# is TRUE
print('\n is sorted df_grp[education_num] mono-increasing? ',df_grp['education_num'].sort_values().is_monotonic_increasing,'\n')

# create mono_increasing from grouped dataframe
df_grpsorted = df_grp.sort_values(by=['education_num'], ascending=True).reset_index(drop=True)

#   #create a sequential number in new column, and add to grouped and sorted df#
# create sequential range on length of grouped dataframe and convert numpy.ndarry to Series
seq_gen = pd.Series( np.arange(1, len(df_grp)+1) )

df_grpsorted['c_monoincrease']= seq_gen

df_grpsorted.info()

# create dataframe on merge of original and grouped-with-sequential number dataframes on "education"
df_merged = df.merge(df_grpsorted,on=['education'],how='inner', suffixes=('', '_y'))

df_merged[['workclass','education','education_num','c_monoincrease']] \
   .sort_values(by=['education_num'], ascending=True) \
   .head()

df_merged.info()

print(pd.DataFrame(df_merged[['workclass','education','education_num','c_monoincrease']],index = [1,6000,16000,17800]))

# compute correlation    
print('\ncorr on education_num - c_monoincrease: ',df_merged['education_num'].corr(df_merged['c_monoincrease']))
