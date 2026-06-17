from pymongo import MongoClient


# MongoDB Connection
client = MongoClient(
    "mongodb://localhost:27017"
)


# Database
db = client["auth_db"]


# Users Collection
users_collection = db["users"]


# Tea Collection
teas_collection = db["teas"]