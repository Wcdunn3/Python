import datetime as dt
import matplotlib as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2017,1,1)


df = web.DataReader('F','yahoo',start,end)
print(df.head())
#Print last 5 lines of dataframe 
print(df.tail())


df.to_csv('ford.csv')
