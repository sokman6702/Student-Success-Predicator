import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("archive/student_performance_100.csv")

print("missing values ")
print(df.isnull().sum())

le=LabelEncoder()
df['internet']=le.fit_transform(df["internet"])
df['passed']=le.fit_transform(df["passed"])
df['study hours']=le.fit_transform(df["study hours"])
df['sleep hours']=le.fit_transform(df["sleep hours"])



print("after encoding : ")
print(df.head())

print("data types after encoding ")
print(df.dtypes)
