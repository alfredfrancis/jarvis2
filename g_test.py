from sklearn.externals import joblib
import numpy as np
import pandas as pd
import warnings
#ignore warnings on Deprecated functions
warnings.simplefilter('ignore', DeprecationWarning)

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

jarvis = joblib.load('jarvis.pkl')

features_test_input = []
print("light,time,motion")
for i in range(3):
	features_test_input.append(input())

#predicting target value
target_predicted = jarvis.predict(features_test_input)

print(target_predicted)