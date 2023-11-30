#21a
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')
df

sns.countplot(x=df["Species"])
plt.title('Frequency of Three Species')
plt.legend()
plt.show()

plt.hist(x=df["Species"])

#s21b
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')
df

sns.countplot(x=df["Species"])
plt.title('Frequency of Three Species')
plt.legend()
plt.show()

plt.hist(x=df["Species"])