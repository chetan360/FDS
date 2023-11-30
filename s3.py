#s3a
import pandas as pd
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')
df

sns.boxplot(x="Species", y="PetalLengthCm", data=df )
plt.show()

sns.boxplot(x="Species", y="SepalWidthCm", data=df )
plt.show()

sns.boxplot(x="Species", y="PetalLengthCm", data=df )
plt.show()

sns.boxplot(x="Species", y="PetalWidthCm", data=df )
plt.show()


#s3b
from matplotlib import pyplot as plt
import numpy as np

cars = ['FDS', 'BLCOKCHAIN', 'TCS','SYSPRO', 'JAVA', 'INTERNET PROGRAMMING']
 
data = [23, 17, 35, 29, 12, 33]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)
 
# show plot
plt.show()