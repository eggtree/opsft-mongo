from pymongo import MongoClient
import os


def index():
    client = MongoClient(os.environ['MONGO_HOST'],
                         int(os.environ['MONGO_PORT']))
    # check whether a username/pwd are set and if so
    # connect with authentication, otherwise connect without
    # http://docs.mongodb.org/manual/tutorial/enable-authentication/
    db = client[os.environ['MONGO_DB']]

    mongo_user = os.environ.get('MONGO_USER')
    mongo_pwd = os.environ.get('MONGO_PWD')
    if mongo_user and mongo_pwd:
        db.authenticate(mongo_user, mongo_pwd)

    coll = db['issuer']
    print coll.count()
    return coll.count()

if __name__ == '__main__':
    index()
