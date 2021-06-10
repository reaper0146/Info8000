#Soumya Pal
#Assignment 3 part 1

import pandas as pd

data_path = "Assignment3_data/"
df_density = pd.read_csv(data_path + 'densities.csv')
df_iris = pd.read_csv(data_path + 'iris.data')
df_county = pd.read_excel(data_path + 'agriculture_20.xlsx ', sheet_name= 'selected_facts', header = 7) #, skiprows=7)#, delimiter=',') #, na_values='NUL')

df_density.set_index("identifier", inplace=True)
df_county.rename(columns={df_county.columns.values[0]: "county"})
df_county.dropna(inplace=True)
df_state = df_county.iloc[[-1]]
df_county = df_county[:-1]

df_iris.columns = ["sepal_length_cm", "sepal_width_cm", "petal_length_cm", "petal_width_cm", "species"]

print(df_density)
print("\n")
print(df_iris)
print("\n")
print(df_county)
print("\n")
print(df_state)
