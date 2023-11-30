#s20a
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

#s20b
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

X=np.random.randint(1,1000,10)
X

df=pd.DataFrame(X , index=labels)
df

df.loc['d']=[11]
df

df.loc['h']=[79]
df

df.loc['ah']=[19]
df

df.rename(columns = {'0':'TEST'}, inplace = True)
df

sns.boxplot(data=df,x=df[0