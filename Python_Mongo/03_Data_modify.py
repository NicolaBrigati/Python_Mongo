import pymongo
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
query = {"nome": "Pinotto"}
value = {"$set": {"nome": "Giovanni"}}
result = userscollection.update_one(query, value)
print(result.upserted_id)

#modify per id
#upserted = non esisteva ma è stato creato/modificato
query = {"_id": ObjectId("678e9ee95e1a3d6e8058f407")}
value = {"$set": {"nome": "Francisco", "eta" : 33}}
result = userscollection.update_one(query, value)
print(result.upserted_id)

#modify age > x
query = {"eta": {"$gt": 30}} #filter for a query
value = {"$set": {"nome": "Leonardo"}}
result = userscollection.update_many(query, value)
print(result.modified_count)

