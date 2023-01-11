import pandas as pd
df = pd.read_csv("C:\\Users\Avinash Rana\\Downloads\\mokesh.csv")
print(df.head(5))
print(df['horsepower'].value_counts())

print(df.isnull().sum().sum())
print(df['horsepower'].isnull().sum())

df = df['horsepower'] = df['horsepower'].fillna(80)
print(df['horsepower'].isnull().sum())

df['horsepower'] = df['horsepower'].replace('?',59)
print(df['horsepower'])
