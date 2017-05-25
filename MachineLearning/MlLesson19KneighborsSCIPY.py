import warnings 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
from math import sqrt
import pandas as pd
import random 

style.use('fivethirtyeight')


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >=k:
        warnings.warn('K should be smaller')
    distances = []
    for group in data:
        for features in data[group]:
# Lazy numpy implementation
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            # add result to final list 
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    #print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][0] / k
      
    #print(vote_result,confidence)  

    return vote_result, confidence



df = pd.read_csv("BreastCancerData.data")
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).values.tolist()
#print(full_data[:5])
random.shuffle(full_data)
#print(20*'#')
#print(full_data[:5])


test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
#splitting data for testing/training
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])


for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0 
total = 0

for group in test_set:
    for data in test_set[group]:
        vote, confidence = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct +=1
        else:
            print(confidence)
        total +=1

print('Accuracy:', correct/total)




