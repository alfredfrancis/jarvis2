from sklearn.externals import joblib
import warnings
# ignore warnings on Deprecated functions
warnings.simplefilter('ignore', DeprecationWarning)

jarvis = joblib.load('jarvis.pkl')

features_test_input = []
print("light,time,motion")

for i in range(3):
    features_test_input.append(input())

# predicting target value
target_predicted = jarvis.predict(features_test_input)

print(target_predicted)
