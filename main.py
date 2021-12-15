import pandas as pd


df= pd.read_csv('C:\\Users\\이창현\\PycharmProjects\\pythonProject1\\weather.csv',sep=',',thousands=',')
print(df.head())