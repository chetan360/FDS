#s1a
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Iris.csv')
df
df['Species'].value_counts().plot.pie()
plt.title('Frequency of Three Species')
plt.legend()
plt.show()

#s1b
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("wineQualityReds.csv")
data.head()

data.info()

data.describe()