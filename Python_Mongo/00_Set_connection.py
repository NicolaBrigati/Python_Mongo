import pymongo
from pymongo import MongoClient

#import default connection from MongoDb
client = MongoClient('localhost', 27017)
db = client.pymongo

# import collections
userscollection = db.users
productscollection = db.products

#verify the connections
print(client.server_info())