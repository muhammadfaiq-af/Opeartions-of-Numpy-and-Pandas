import numpy as np
import pandas as pd

df = pd.read_excel("book.xlsx")
print(df)

# Question 1
x = df.iloc[: , -1].values
count = 0
for i in x:
    if i > 2:
        b = count = count + 1
print("No of Rows Grester Than 2 : " , b)

# Question 2

print("No of Rows : " , len(x))

# Question 3

x = df.iloc[: , -2].values
count = 0
for i in x:
    if i > 200:
        c = count = count + 1
print("No of Rows Grester Than 200 : " , c)

# Question 4

df['Score'][1] = 700
print(df)
df.to_excel('Book3.xlsx')

# Question 5

print("No of Attempts : " , len(x))

# Question 6

Score = df['Score'].values
Score_avg = np.average(Score)
print("Score_avg" , Score_avg)

# Question 7

Score = df['Score'].values
Score_min = np.min(Score)
print("Score_min" , Score_min)

Score = df['Score'].values
Score_max = np.max(Score)
print("Score_max" , Score_max)