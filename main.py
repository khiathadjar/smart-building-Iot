from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from base import things_collection
from bson import ObjectId
import uuid # Important pour générer l'ID que ta base exige

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend SmartLocate Opérationnel"}

# --- RECHERCHE ET AFFICHAGE (Utilisé par index.html et objets.html) ---
@app.post("/things/search")
def search_things(data: dict = Body(...)):
    search_query = data.get("search_query", "")
    query = {"name": {"$regex": search_query, "$options": "i"}}
    results = list(things_collection.find(query))
    for item in results:
        item["_id"] = str(item["_id"])
    return results

# --- AJOUTER UN OBJET (Utilisé par ajouter-objet.html) ---
@app.post("/things/add")
def add_thing(data: dict = Body(...)):
    try:
        # 1. Préparation pour respecter ta validation MongoDB (Code 121)
        # On crée un ID unique car ta base refuse l'insertion s'il manque
        generated_id = str(uuid.uuid4())[:8] 

        new_item = {
            "id": generated_id,
            "name": data.get("name"),
            "type": data.get("type"),
            # Transformation en OBJET car ta base refuse les simples textes (strings)
            "location": { "room": data.get("location") }, 
            "description": data.get("description", ""),
            "status": data.get("status", "active")
        }

        # 2. Insertion
        result = things_collection.insert_one(new_item)
        print(f"✅ Objet ajouté dans MongoDB : {data.get('name')}")
        
        return {"message": "Succès", "id": generated_id}

    except Exception as e:
        print(f"❌ Erreur de validation : {e}")
        raise HTTPException(status_code=500, detail="Données non conformes au schéma MongoDB")

@app.post("/login")
def login(data: dict = Body(...)):
    return {"access_token": "test_token", "session": {"access_token": "test_token"}}