import pymongo
from pymongo import MongoClient

# Connessione al client MongoDB
client = MongoClient('localhost', 27017)

# Connessione al database e alle collezioni
db = client.pymongo
userscollection = db.users

# Inserisce gli utenti solo se la collezione è vuota
if userscollection.count_documents({}) == 0:
    userscollection.insert_many(users)

# Recupera tutti i documenti dalla collezione
all_users = userscollection.find()

# Stampa dei documenti recuperati
print("Tutti gli utenti:")
for user in all_users:
    print(user)
