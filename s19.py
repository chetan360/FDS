#s19

import pandas as pd
data  = {'name': ['ise', 'riyas', 'koniko', 'akino', 'idna', 'huma', 'xinovia', 'zero two', 'eren', 'madara'],
        'percentage': [65, 59, 75, 59.63, 89, 72, 64.5, 71, 87, 81],
        'age': [17,19,20,19,19,18,19,17,18,20]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data , index=labels)
df


print(df.shape)
print("\nData Type:")
print(type(df))

rows = len(df.axes[0])
cols = len(df.axes[1])

print("Number of Rows: " + str(rows))
print("Number of Columns: " + str(cols))

df.describe()

dict = {'name':['sukuna', 'saitama','gojo','naruto','itachi'],
        'percentage':[89, 90,67,59,75],
        'age':[19, 18,18,19,19]
       }
  
df1 = pd.DataFrame(dict)
display(df1)
  
newdf = pd.concat([df, df1], ignore_index = True)
newdf.reset_index()
  
display(newdf)

newdf['remarks']=None
newdf
