#s2a
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Data(1).csv")
df.head()

df['salary'].fillna(df['salary'].mean())

#s2b
plt.plot(df['degree_t'], df['salary'])
plt.show() 

#s2c
import pandas as pd
df = pd.read_csv('HeightWeight.csv')
df.head(10)

print(df.tail(10))

print(df.sample(20))

print(df.shape)