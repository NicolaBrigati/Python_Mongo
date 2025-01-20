import pymongo
from pymongo import MongoClient

#import default connection from MongoDb
client = MongoClient('localhost', 27017)
db = client.pymongo
userscollection = db.users
productscollection = db.products

#create a user that is a dict
user = {"nome": "Marco", "cognome": "Verdi"}
result = userscollection.insert_one(user)

#create with #id
user = {"_id": "01", "nome": "Marco", "cognome": "Verdi"}

#create multiple users
users = [
    {"nome": "Luca", "cognome": "Gialli", "eta": 23},
    {"nome": "Gianni", "cognome": "Tucsteno", "eta": 18},
    {"nome": "Pinotto", "cognome": "Serra", "eta": 35},
    {"nome": "Franco", "cognome": "Neri", "eta": 27},
    {"nome": "Rodolfo", "cognome": "Giotti", "eta": 30},
]
result = userscollection.insert_many(users)

print(result)
#see the object id created:
print(result.inserted_ids)