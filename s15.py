#s15a
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

#s15b
from matplotlib import pyplot as plt
import numpy as np

cars = ['FDS', 'BLCOKCHAIN', 'TCS',
        'SYSPRO', 'JAVA', 'INTERNET PROGRAMMING']
 
data = [23, 17, 35, 29, 12, 33]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)
 
# show plot
plt.show()