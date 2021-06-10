#Soumya Pal
#Assignment 3 part 1

import pandas as pd
import math as m

data_path = "Assignment3_data/"
df = pd.read_csv(data_path + '/titanic.csv')
df.set_index("PassengerId", inplace=True)
print(df.isna().any())

df.drop(columns = ["Cabin"], axis=1, inplace=True)

age_nan = df.isnull().sum()["Age"]

df.dropna(subset=['Embarked'], inplace=True)

avg_age = df['Age'].sum()/(len(df['Age']) - age_nan)

values = {'Age': avg_age}
df.fillna(value=values, inplace=True)


df['FamilySize'] = df["Parch"] + df["SibSp"] + 1

stats_num = df.describe()
stats_cat = df.describe(include='object')
print("\n")
print(stats_num)
print("\n")
print(stats_cat)
df.to_csv('titanic_clean.csv',index=True)