import pandas as pd

df = pd.read_csv("archive/student_performance_100.csv")
print(df)

print("first five rows : ")
print(df.head())

print("information in the data : ")
print(df.info())

print("dataset shape")
print(f'rows:{df.shape[0]},colums :{df.shape[1]}')

print("summary statistics")
print(df.describe(include='all'))

print("missing values :")
print(df.isnull().sum())


                            