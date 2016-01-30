import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#ignore warnings on Deprecated functions
warnings.simplefilter('ignore', DeprecationWarning)

#Reading data from csv file
data = pd.read_csv('datasets/data.csv')
#print(data.head(3))

#setting target value
_bulb2 = data['bulb2']
target = _bulb2.values

#setting features for prediction
numerical_features = data[['light', 'time', 'motion']]

#converting into numpy arrays
features_array = numerical_features.values
#print(features_array)

#80% of the data for training a first model and keep 20% for computing is generalization score
features_train, features_test, target_train, target_test = train_test_split(
    features_array, target, test_size=0.10, random_state=0)

#performing logistic regression,creating model
logreg = LogisticRegression(C=1)
logreg.fit(features_train, target_train)

features_test_input = []
print("light,time,motion")
for i in range(3):
	features_test_input.append(input())

#predicting target value
target_predicted = logreg.predict(features_test_input)

print(target_predicted)
#printing accuracy score of the predicted result
#print(accuracy_score(target_test, target_predicted))