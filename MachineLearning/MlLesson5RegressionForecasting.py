import pandas as pd
import quandl, math,datetime
import numpy as np
#svm- Support vector machine 
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
#importing graphics plotting and styling 
style.use('ggplot')
 
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

#Features = x &  labels = Y
X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out:]



df.dropna(inplace=True)
Y = np.array(df['label'])
Y = np.array(df['label'])

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2)

clf = LinearRegression(n_jobs=5)
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)

# print(accuracy)

forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. close'].plot()
df['forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
