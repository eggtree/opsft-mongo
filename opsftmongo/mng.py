from pymongo import MongoClient
import os


def index():
    # e.g. mongodb://admin:password@127.8.126.130:27017/
    client = MongoClient(os.getenv('MONGO_DB_URL','mongodb://localhost'))
    db = client[os.environ['MONGO_DB_NAME']]
    
    coll = db['issuer']
    print coll.count()
    return coll.count()

if __name__ == '__main__':
    index()
