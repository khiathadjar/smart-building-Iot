import os
from dotenv import load_dotenv
from supabase import create_client

# Charge le fichier .env
load_dotenv("bdd.env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# --- AJOUTE CE PETIT PRINT DE TEST ---
if not SUPABASE_KEY:
    print("❌ ERREUR : La clé Supabase n'est pas chargée. Vérifie bdd.env !")
else:
    print(f"✅ Clé chargée (début) : {SUPABASE_KEY[:10]}...")
# --------------------------------------

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# Fonctions helper pour signup/login
def signup_user(email, password):
    res = supabase.auth.sign_up({"email": email, "password": password})
    return res


def login_user(email, password):
    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return res
