from pymongo import MongoClient

uri = "mongodb://192.168.101.101:32000/?replicaSet=rs0"
client = MongoClient(uri)
