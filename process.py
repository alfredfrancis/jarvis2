import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

warnings.simplefilter('ignore', DeprecationWarning)

#Reading data from csv file
data = pd.read_csv('datasets/data.csv')
#print(data.head(3))

#setting target value
_l2 = data['bulb1']
target = _l2.values

#setting features for prediction
numerical_features = data[['light', 'time', 'motion']]

#converting into numpy arrays
features_array = numerical_features.values
#print(features_array)

#80% of the data for training a first model and keep 20% for computing is generalization score
features_train, features_test, target_train, target_test = train_test_split(
    features_array, target, test_size=0.20, random_state=0)

#performing logistic regression
logreg = LogisticRegression(C=1)
logreg.fit(features_train, target_train)
#target_predicted = logreg.predict(features_test)

#printing accuracy score of the predicted result
#print(accuracy_score(target_test, target_predicted))