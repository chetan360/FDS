#s8
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 


df= pd.read_csv('wineQuality.csv')
df.head()


mu, sd = 0, 1  # mean and standard deviation
s = np.random.normal(mu, sd, 100000)
print("mean: ", np.mean(s))
print("standart deviation: ", np.std(s))
# visualize with histogram
plt.figure(figsize = (10,7))
plt.hist(s, 100)
plt.ylabel("quality")
plt.xlabel("alcohole")
plt.title("Histogram of Wine Quality")
plt.show()