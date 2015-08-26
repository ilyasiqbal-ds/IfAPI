__author__ = 'Ilyas'
# This file keeps the configuration of the application.
# More functionality can be added, for example; routes, constants, etc

import pymongo


# function to get connected to the MongoDB database
def dbConnect():

    client = pymongo.MongoClient("localhost",27017)
    db = client.ifdb

    # returns the db as an object to access collections
    return db

