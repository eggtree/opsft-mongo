from pymongo import MongoClient
import os


def index():
    # when you connect to mongo using a url which includes authentication 
    # information you have to ensure one of the following is true:
    # a) the user exists in the admin database
    # b) the url includes the database where the user exists
    # e.g. MONGO_DB_URL=mongodb://admin:password@127.8.126.130:27017/acaex
    # This is because mongo users are per database, so if your user is
    # not in the admin db you need to pass in at MongoClient initialization
    # time which db to check for authentication info. 
    # Normally you can wait and pick your database to connect to after 
    # MongoClient is initialized
    # Fortunately openshift stores users in the admin db
    client = MongoClient(os.getenv('MONGO_DB_URL','mongodb://localhost'))
    db = client[os.getenv('MONGO_DB_NAME', 'acaex')]
    
    coll = db['issuer']
    print coll.count()
    return coll.count()

if __name__ == '__main__':
    index()
