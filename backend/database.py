from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Collections
portfolio_collection = db.portfolio
services_collection = db.services
projects_collection = db.projects

async def close_db_client():
    client.close()

# Database helper functions
def convert_object_id(item):
    """Convert MongoDB _id to string id"""
    if item and "_id" in item:
        item["id"] = str(item["_id"])
        del item["_id"]
    return item

def convert_object_ids(items):
    """Convert MongoDB _id to string id for list of items"""
    return [convert_object_id(item) for item in items]