
		result = db.data_reading.insert(
			[
				{
					"light":40,
					"motion":1,
					"temprature":30,
					"humidity":40,
					"time":23,
					"bulb1":1,
					"bulb2":2,
					"fan1":1
				}		
			])

You can use:

>>> from sklearn.externals import joblib
>>> joblib.dump(clf, 'my_model.pkl', compress=9)
And then later, on the prediction server:

>>> from sklearn.externals import joblib
>>> model_clone = joblib.load('my_model.pkl')



>>> import pickle
>>> s = pickle.dumps(clf)
>>> clf2 = pickle.loads(s)
>>> clf2.predict(X[0])
array([0])
>>> y[0]
0


mongoimport -d test -c data_reading --type csv --file dataset/data.csv --headerline
