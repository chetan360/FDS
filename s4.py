#s4a
import numpy as np

from matplotlib import pyplot as plt

X=np.random.randint(1,1000,50)
X

fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(X)
 

plt.show()

plt.plot(X)  # Plot the chart
plt.show()


plt.scatter(X,X)
plt.show()



plt.boxplot(X)
plt.show()


#s4b
import pandas as pd
data = pd.read_csv("Iris.csv")
print("Shape of the data:")
print(data.shape)
print("\nData Type:")
print(type(data))
print("\nFirst 3 rows:")
print(data.head(3))
