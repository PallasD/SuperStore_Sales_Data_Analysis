from pydoc import describe

import pandas as pd
from pandas import read_csv

df = pd.read_csv('Sample - Superstore.csv',index_col=0, encoding='latin1',)

print(df.info)
print(df.isnull().sum())

print("duplicate lines : ",df.duplicated().sum())
duplicates = df[df.duplicated()]
print(duplicates)

df = df.drop_duplicates()

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')

print(df.isna().sum())

df.to_csv('cleaned_SuperStore', index=False)
