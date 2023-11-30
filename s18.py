#s18a
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

#s18b
import pandas as pd
df = pd.read_csv('HeightWeight.csv')
df.head(10)

print(df.tail(10))

print(df.sample(20))

print(df.shape)
