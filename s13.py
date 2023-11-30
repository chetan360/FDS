#s13a
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("Iris.csv")
fig = iris[iris.Species=='Iris-setosa'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='orange', label='Setosa')
iris[iris.Species=='Iris-versicolor'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='blue', label='versicolor',ax=fig)
iris[iris.Species=='Iris-virginica'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='green', label='virginica', ax=fig)
fig.set_xlabel("Petal Length")
fig.set_ylabel("Petal Width")
fig.set_title(" Petal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(12,8)
plt.show()

#s13b
import numpy as np
a = np.arange(25).reshape((5,5))
print("Original flattened array:")
print(a)
print("Maximum value of the above flattened array:")
print(np.amax(a))
print("Minimum value of the above flattened array:")
print(np.amin(a))