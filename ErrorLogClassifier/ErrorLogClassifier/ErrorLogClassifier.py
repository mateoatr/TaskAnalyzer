import numpy as np
import pandas as pd
import pickle

from difflib import SequenceMatcher
from sklearn import svm, preprocessing, cross_validation

data_vectors = []
target_vector = []

data = pd.read_csv("data.csv")
target = pd.read_csv("target.csv")
for i in range(0, 240):
    data_vectors.append(data[str(i)].tolist())
    target_vector.append(target[str(i)].tolist())
target_vector = np.array([i for sublist in target_vector for i in sublist])
data_vectors = np.array(data_vectors)

X = data_vectors
X = preprocessing.scale(X)

y = target_vector

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

linearClf = svm.SVC(kernel='linear')
linearClf.fit(X_train, y_train)
linear_confidence = linearClf.score(X_test, y_test)
print("Linear confidence: " + str(linear_confidence))

with open('linearClf.pickle','wb') as f:
    pickle.dump(linearClf, f)
