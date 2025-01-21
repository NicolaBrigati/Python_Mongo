from itertools import count

import pymongo
from bson import ObjectId
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.pymongo
userscollection = db.users
productscollection = db.products

if userscollection.count_documents({}) == 0:
    userscollection.insert_many(users)

#count num users with cities
count_users_with_city = userscollection.count_documents({"citta": {"$exists": True}})
print(f"Numero di utenti con il campo 'citta': {count_users_with_city}")

#print user with city
citta_users = userscollection.find({"citta": {"$exists": True}})
print("Utenti con città:")
for user in citta_users:
    print(user)

# > $regex > check on string
a_citta_users = userscollection.find({"citta": {"$regex": ".*a.*i.*", "$options": "i"}})
print("Utenti con 'a' e 'i' nella città:")
for user in a_citta_users:
    print(user)


# > $or $and > check on string
animal_users = userscollection.find({
    "$or": [
        {"animal": {"$regex": "o$"}},  # Cerca campi "animal" che terminano con "o"
        {"citta": {"$exists": True}}  # Cerca campi "citta" che esistono
    ]})
print("Utenti con 'animal' che termina in 'o' o con 'citta' definita:")
for user in animal_users:
    print(user)