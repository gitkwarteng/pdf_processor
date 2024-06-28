from pymongo import MongoClient
from mongoengine import connect

def get_db_handle(db_name, host='localhost', port=27017, username=None, password=None):

 client = MongoClient(host=host,
                      port=int(port),
                      username=username,
                      password=password
                     )
 db_handle = client['db_name']
 return db_handle, client
