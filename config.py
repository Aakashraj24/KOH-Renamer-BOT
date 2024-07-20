import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29201763")

API_HASH = os.environ.get("API_HASH", "10d0e463862b3d0e4c2441aa70b73c8f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7241587663:AAHrvXelS3YBr9_6i0srJjIJuAWQz0--Aso") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002155925318") 

DB_NAME = os.environ.get("DB_NAME","kohbots")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://<username>:jjv9k0LxbBFIVH7f@cluster0.fyf3gsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5300021755').split()]

PORT = os.environ.get("PORT", "8080")
