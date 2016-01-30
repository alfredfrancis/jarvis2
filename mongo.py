from pymongo import MongoClient
import numpy as np
from pandas import DataFrame

#MongoDB interface class
class Dataset:

	#constructor
	def __init__(self,dbname):
		client = MongoClient()
		self.db = getattr(client,dbname)

	def set_collection(self,cltname):
		#Specifying collection name
		self.cltname = cltname

	def insert_row(self,row = []):
		return self.db[self.cltname].data_reading.insert(row)

	def delete_row(self):
		pass

	def retrive_set(self):
		#reading all fields except _id
		cursor = self.db[self.cltname].find({},{ "_id":0 })
		#converting cursor object to pandas array
		df = DataFrame(list(cursor))
		#returning NumPy array
		return df.values
