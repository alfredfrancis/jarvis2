from sklearn.externals import joblib
import warnings
# ignore warnings on Deprecated functions
warnings.simplefilter('ignore', DeprecationWarning)

jarvis = joblib.load('jarvis.pkl')

features_test_input = [50,5,0]
print("light,time,motion")


# predicting target value
target_predicted = jarvis.predict(features_test_input)

print(target_predicted)
