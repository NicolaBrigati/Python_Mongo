import pymongo
from pymongo import MongoClient

#import default connection from MongoDb
client = MongoClient('localhost', 27017)
db = client.pymongo
print(client.server_info())