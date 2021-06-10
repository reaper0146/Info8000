#Soumya Pal
#Assignment 1 part 2

import pandas as pd
import seaborn as sns
#import urllib.parse as p
import matplotlib.pyplot as plt

sheet_id = "1QzamD-Lzj2UUMjiQllywRw9sbWIsChEsFSNBjtq8_NI"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
#url = p.quote(url1, safe='/', encoding=None, errors=None)
#url = url.parse(':')
df = pd.read_csv(url)

df.columns = ["Timestamp", "Programming", "Python", "R"]
df = df.drop(columns=["Timestamp"])
df = df.melt(var_name="skill")

g= sns.catplot(kind='count', x='value', col = 'skill', data=df)
g.fig.suptitle("Different programming language Skill level and Count",fontweight="bold",fontsize=14)
plt.tight_layout(rect=(0,0,1,.9))
plt.show()