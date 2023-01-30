import pandas as pd
import csv

# load original dataset
df = pd.read_csv('../test_income_data1.csv')

# show shape
print(df.shape)

# original dataset with duplicate rows removed
d_unq = df.drop_duplicates(keep='first', ignore_index=True)

# create 3 sampled dataframes--approx 10% each for set operations
#  NOTE: explicitly showing default sampling method, without replacement
df_1 = d_unq.sample(n = 3250, replace=False)
df_2 = d_unq.sample(n = 3250, replace=False)
df_3 = d_unq.sample(n = 3250, replace=False)

# create csv files from each of 3 samples
df_1.to_csv('set_income_data1.csv',sep=',',quotechar='"',index=False,quoting=csv.QUOTE_NONNUMERIC)

df_2.to_csv('set_income_data2.csv',sep=',',quotechar='"',index=False,quoting=csv.QUOTE_NONNUMERIC)

df_3.to_csv('set_income_data3.csv',sep=',',quotechar='"',index=False,quoting=csv.QUOTE_NONNUMERIC)

