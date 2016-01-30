
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

import warnings
#ignore warnings on Deprecated functions
warnings.simplefilter('ignore', DeprecationWarning)

rf = RandomForestRegressor()
rfc = RandomForestClassifier(max_depth = 4)

#Reading data from csv file
data = pd.read_csv('datasets/data.csv')

#setting target value
_bulb2 = data['bulb2']
target = _bulb2.values


idx = range(len(target))
np.random.shuffle(idx)

#setting features for prediction
numerical_features = data[['light', 'time', 'motion']]

#converting into numpy arrays
features_array = numerical_features.values

rf.fit(features_array, target)
rfc.fit(features_array, target)

features_test_input = []
print("light,time,motion")
for i in range(3):
	features_test_input.append(input())

print "Bulb2 state prediction(using regressor):", rf.predict(features_test_input)
print "Probability :", rfc.predict(features_test_input)