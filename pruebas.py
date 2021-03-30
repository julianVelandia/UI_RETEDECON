import pandas as pd


df = pd.read_csv('D.csv')
df_as_dataframe = pd.DataFrame(df)
df.drop(['Nombre'],axis=1)
print(df)
