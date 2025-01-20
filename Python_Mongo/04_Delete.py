from bson import ObjectId
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.pymongo
userscollection = db.users
productscollection = db.products

users = [
    {"nome": "Luca", "cognome": "Gialli", "eta": 23},
    {"nome": "Gianni", "cognome": "Tucsteno", "eta": 18},
    {"nome": "Pinotto", "cognome": "Serra", "eta": 35},
    {"nome": "Franco", "cognome": "Neri", "eta": 27},
    {"nome": "Rodolfo", "cognome": "Giotti", "eta": 30},
]

#single delete
query = {"_id": ObjectId("678e9ee95e1a3d6e8058f409")}
result = userscollection.delete_one(query)
print(result.deleted_count)

#delete age > x
query = {"eta" : {"$lt" : 19}}
result = userscollection.delete_many(query)
print(result.deleted_count)

#delete all the list of collection
#query = {}
#result = userscollection.delete_many(query)
#print(result.deleted_count)