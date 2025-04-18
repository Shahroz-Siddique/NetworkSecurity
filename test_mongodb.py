from pymongo import MongoClient

uri = "mongodb+srv://shahrozsiddique066:Shahroz321@cluster0.ehcvain.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, serverSelectionTimeoutMS=10000)  # 10 seconds timeout

try:
    client.admin.command('ping')
    print("Connected successfully!")
except Exception as e:
    print("Connection error:", e)
