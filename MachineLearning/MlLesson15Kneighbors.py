import warnings 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
from math import sqrt

style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}

new_features = [5,7]


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
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    
    return vote_result

result = k_nearest_neighbors(dataset, new_features, k=3)

print(result)

# One liner for loop to iterate through the list of lists
[[plt.scatter(ii[0],ii[1], s=100,color=result)for ii in dataset[i]] for i in dataset]
#Add in the new feature to plot 
plt.scatter(new_features[0], new_features[1])
plt.show()
