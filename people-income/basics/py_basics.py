import numpy as np
import pandas as pd


df = pd.read_csv('../test_income_data1.csv')

# show shape and describe columns
print(df.shape)
df.info()

# Make a list of all variables with classes
vars_list = list(df.select_dtypes(include=['object']).columns)

# describe non-numeric columns
for v in vars_list:
    num_classes = df[v].nunique()
    print('There are {} classes in the \'{}\' table. '.format(num_classes,v))

          # Simple query
# select 5 unique records  
df['native_country'].unique()[0:5]

# sort list as lexicographic 5 unique records
sorted(df['native_country'].unique())[0:5]

# select 5 records with simple-predicate
df[df['native_country']=='Cambodia']
# select 5 records of named variablescolumns with simple-predicate
df[df['native_country']=='Cambodia'][['age','workclass','education','education_num']][0:5]

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

# with simple-predicate, group-by on multiple columns having count specified and sorted by a selection
df[(df['income'] == '>50K')].groupby(['education_num','education', 'occupation']).size() \
    .loc[lambda x: x >30].reset_index() \
    .sort_values(by='education_num', ascending=False)

#     # subquery using max() 
# count(*) with predicate where  max(capital_loss) 
df[ (df['capital_loss']) == (df['capital_loss'].max()) ]['capital_loss'].size
# select workclass, sex, age   with predicate where  max(capital_loss) 
df[ (df['capital_loss']) == (df['capital_loss'].max()) ][['workclass','sex','age']]

