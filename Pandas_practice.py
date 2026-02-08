import pandas as pd

df = pd.read_csv("train.csv")  # Titanic dataset

print(df.head())
print(df.isnull().sum())

df["Age"].fillna(df["Age"].median(), inplace=True)

print("Missing values after cleaning:")
print(df.isnull().sum())
