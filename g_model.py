import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
from sklearn.externals import joblib
#ignore warnings on Deprecated functions
warnings.simplefilter('ignore', DeprecationWarning)

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



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



#performing logistic regression,creating model
logreg = LogisticRegression(C=1)
logreg.fit(features_array, target)

#dump generated model to file
joblib.dump(logreg, 'jarvis.pkl', compress=9)