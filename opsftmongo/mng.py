from pymongo import MongoClient
import os


def index():
    #print 1
    #print os.getenv('OPENSHIFT_MONGODB_DB_URL','blah')
    #print os.environ['MONGO_HOST']
    client = MongoClient(os.getenv('MONGO_DB_URL','mongodb://localhost'))
    # check whether a username/pwd are set and if so
    # connect with authentication, otherwise connect without
    # http://docs.mongodb.org/manual/tutorial/enable-authentication/
    #print 2
    db = client[os.environ['MONGO_DB_NAME']]

   # mongo_user = os.environ.get('MONGO_USER')
    #mongo_pwd = os.environ.get('MONGO_PWD')
    #print 3
    #if mongo_user and mongo_pwd:
    #    db.authenticate(mongo_user, mongo_pwd)
    #print 4
    coll = db['issuer']
    print coll.count()
    return coll.count()

if __name__ == '__main__':
    index()
