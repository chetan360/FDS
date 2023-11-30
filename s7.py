#s7a
import pandas as pd
data = pd.read_csv("Sales Data.csv",encoding='latin1')
data

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown='ignore')

encoder_df = pd.DataFrame(encoder.fit_transform(data[['COUNTRY']]).toarray())

#merge one-hot encoded columns back with original DataFrame
final_df = data.join(encoder_df)

final_df

from sklearn.preprocessing import LabelEncoder

#s7b
le = LabelEncoder()

data.SALES = le.fit_transform(data.SALES)
data

