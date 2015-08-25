__author__ = 'Ilyas'

import pymongo




def dbConnect():

    client = pymongo.MongoClient("localhost",27017)
    db = client.ifdb

    return db

