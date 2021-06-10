import pandas as pd
import math as m

data_path = "Assignment3_data/"
df = pd.read_csv(data_path + 'titanic_clean.csv')
df.set_index("PassengerId", inplace=True)
df_sex_mean = df.groupby(['Sex']).mean() 

df_paid_most = df.nlargest(10,'Fare')

df_ticket = df.groupby(['Ticket'])

df_ticket.transform(lambda x: (sum(x) for y in x))
df_ticket = df_ticket.sum()

df_ticket.rename(columns={"Fare" : "TicketFare"}, inplace=True)
df_ticket.drop(columns=["Survived","Pclass","Age","SibSp","Parch", "FamilySize"], inplace=True)

df = pd.merge(df,df_ticket, how = 'left', on='Ticket')  #, right_index= False)#, ignore_index=True)

df_paid_most_together = df.nlargest(10,"TicketFare")
print(df_paid_most)
print("\n")
print(df_sex_mean)
print("\n")
print(df_paid_most_together)
