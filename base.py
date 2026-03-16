from pymongo import MongoClient  # <--- CETTE LIGNE EST OBLIGATOIRE
from dotenv import load_dotenv
import os

# Charger les variables du fichier bdd.env
load_dotenv("bdd.env")

MONGO_URI = os.getenv("MONGO_URI")

# On ajoute un timeout pour ne pas attendre 30 secondes si la connexion échoue
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

db = client.smart_building
things_collection = db.things

# TEST DE CONNEXION : On essaie de "pinger" la base de données
try:
    client.admin.command('ping')
    print("✅ MongoDB est connecté !")
except Exception as e:
    print(f"❌ Erreur de connexion MongoDB : {e}")