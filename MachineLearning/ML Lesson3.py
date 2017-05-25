import pandas as pd
import quandl
import math

df = quandl.get('Wiki/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df ['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100 
df ['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100 

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
#we're predicting forecast_col
forecast_col = 'Adj. Close'
#Backfilling empty slots 
df.fillna(-99999, inplace=True)
#Rounds up to nearest whole integer 
forecast_out = int(math.ceil(.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail())
