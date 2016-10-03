import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
#svm- Support vector machine 

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
X = np.array(df.drop['label'],1)
Y = np.array(df['label'])
X = preprocessing.scale(X)
Y = np.array(df['label'])

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2)

clf = LinearRegression(n_jobs=5)
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)

print(accuracy)
