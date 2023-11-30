#s10a
import pandas as pd
df = pd.read_csv('HeightWeight.csv')
print(df)
m1=df['Height'].mean()
m2 = df['Weight'].mean()
med1 = df['Height'].median()
med2 = df['Weight'].median()
print('mean of Height: ' + str(m1))
print('mean of Weight: ' + str(m1))
print('Median of Height: ' + str(med1))
print('Median of Weight: ' + str(med2))

#s10b
def distancesum (x, y, n):
    sum = 0
     
    for i in range(n):
        for j in range(i+1,n):
            sum += (abs(x[i] - x[j]) +
                        abs(y[i] - y[j]))
     
    return sum
 

x = [ -1, 1, 3, 2 ]
y = [ 5, 6, 5, 3 ]
n = len(x)
print(distancesum(x, y, n) )
