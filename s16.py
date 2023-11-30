#s16a
from matplotlib import pyplot as plt
import numpy as np

cars = ['FDS', 'BLCOKCHAIN', 'TCS',
        'SYSPRO', 'JAVA', 'INTERNET PROGRAMMING']
 
data = [23, 17, 35, 29, 12, 33]
 

fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)
 

plt.show()


#16b


import pandas as pd
data  = {'name': ['saitama', 'gojo', 'naruto', 'sukuna', 'itachi', 'madara', 'riyas', 'koniko', 'akino', 'idena'],
        'percentage': [65, 59, 75, 59.63, 89, 72, 64.5, 71, 87, 81],
        'age': [17,19,20,19,19,18,19,17,18,20]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data , index=labels)
df
avg=sum(df['percentage'])/len(df['percentage'])
print("Average of Percentages :",avg)
avg=sum(df['age'])/len(df['age'])
print("Average of age :",avg)
