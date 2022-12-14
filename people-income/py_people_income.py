import numpy as np
import pandas as pd


df = pd.read_csv('./test_income_data1.csv')

# show shape and describe columns
df.shape
df.info()

# Make a list of all variables with classes
vars_list = list(df.select_dtypes(include=['object']).columns)

# describe non-numeric columns
for v in vars_list:
    num_classes = df[v].nunique()
    print('There are {} classes in the \'{}\' table. '.format(num_classes,v))

          # Simple query
# select 5 unique records  
df['native-country'].unique()[0:5]

# sort list as lexicographic 5 unique records
sorted(df['native-country'].unique())[0:5]

# select 5 records with simple-predicate
df[df['native-country']=='Cambodia']
# select 5 records of named variablescolumns with simple-predicate
df[df['native-country']=='Cambodia'][['age','workclass','education','education-num']][0:5]

         # group-by
df.groupby('workclass')  # dataframe-object

# dataframe-object with statistics 
df.groupby('workclass').describe()

# group-by selected column-field with count of classes
df.groupby('workclass').size().reset_index(name='counts')
     # or
df.groupby(['workclass']).workclass.count()

# group-by on two fields with counts
df.groupby(['sex','workclass']).size()

# group-by sorted by frequency of classes
df.groupby('workclass').size().sort_values(ascending=False).reset_index(name='count-is')

# group-by sorted by frequency of classes having count specified
df.groupby(['workclass']).workclass.count().sort_values(ascending=False).loc[lambda x: x < 100].reset_index(name='count-is')

df.groupby('sex')['workclass'].value_counts().sort_values(ascending=False).loc[lambda x: x < 100].reset_index(name='count-is')

#     # subquery using max() 
# count(*) with predicate where  max(capital_loss) 
df[ (df['capital-loss']) == (df['capital-loss'].max()) ]['capital-loss'].size
# select workclass, sex, age   with predicate where  max(capital_loss) 
df[ (df['capital-loss']) == (df['capital-loss'].max()) ][['workclass','sex','age']]

