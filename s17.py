#s17a

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
iris = pd.read_csv("Iris.csv")
#Drop id column
iris = iris.drop('Id',axis=1)
#Convert Species columns in a numerical column of the iris dataframe
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
iris.Species = le.fit_transform(iris.Species)
x = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values
plt.scatter(x[:,0], x[:, 3], c=y, cmap ='flag')
plt.xlabel('Sepal Length cm')
plt.ylabel('Petal Width cm')
plt.show()

#s17b
import pandas as pd
import numpy as np

exam_data  = {'name': ['ABC', 'DEF', 'AAAA', 'DDDD', 'CCCC', 'PQR', 'QWERTY', 'XYZ', 'PQQR', 'JKLM'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'result': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)

#s17b
import pandas as pd
import numpy as np

exam_data  = {'name': ['ABC', 'DEF', 'AAAA', 'DDDD', 'CCCC', 'PQR', 'QWERTY', 'XYZ', 'PQQR', 'JKLM'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'result': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)
