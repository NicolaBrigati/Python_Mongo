#select doc
#find one, find all, find fields
#find query
#sort asc desc
#limit

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

#import default connection from MongoDb
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


#find one
result = userscollection.find_one()
print(result)

#find all > id insered
result = userscollection.find()
for users in result:
    print(users)

#find fields
result = userscollection.find({}, {"nome": 1})
result = userscollection.find({}, {"_id": 0, "nome": 1})
for users in result:
    print(users)

#find specifics MongoEngine Mongoose > you don't need to clarify the Obj id
#so here you need to import "from bson.objectid import ObjectId"
result = userscollection.find({"_id": ObjectId("678e916909d64408334a7535")})
for users in result:
    print(users)

result = userscollection.find({"nome": "Luca"})
for users in result:
    print(users)


#query on age > x
query = {"eta": {"$gt": 20}}
result = userscollection.find(query)
for users in result:
    print(users)

print()

query = {"eta": {"$lt": 19}}
result = userscollection.find(query)
for users in result:
    print(users)

print()

#sort asc e desc 1 or -1
query = {"eta": {"$lt": 19}}
result = userscollection.find().sort("eta", 1)
for users in result:
    print(users)

print()

#sort asc e desc 1 or -1
query = {"eta": {"$lt": 19}}
result = userscollection.find().sort("nome", -1)
for users in result:
    print(users)

print()
#limit
query = {"eta": {"$lt": 19}}
result = userscollection.find().sort("nome", -1).limit(2)
for users in result:
    print(users)