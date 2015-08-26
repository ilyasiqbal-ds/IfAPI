__author__ = 'Ilyas'
# This is the main application file which creates JSON based APIs
# Flask is the the framework which has been used while developing
# this application, because of it's strength, community and ease
# of use while building API platforms.
# Pymongo is a MongoDB driver which has been used in order to fetch
# saved data from MongoDB engine.


import json
from flask import Flask, jsonify, request
from flask import make_response
from bson.json_util import dumps
import Config


application = Flask(__name__)
# application.debug=True

# Connecting to MongoDB
db = Config.dbConnect()




# Setting up the rout to access JSON data
@application.route('/if/api/v1.0/profile', methods=['GET'])


# This function will fetch all the profiles from ifcollection, if there
# are no request parameters are passed. Otherwise, filtered result will
# be shown!

def get_profiles():

    # json_docs, is being used to append multiple json docs in following for loop
    json_docs = []

    # numSales, is the field filter, which is set in the URL
    if 'numSales' in request.args:
        profiles = db.ifcollection.find({'numSales': request.args['numSales']}, {'_id': False})

    # genderPred, is the field filter, which is set in the URL
    elif 'genderPred' in request.args:
        profiles = db.ifcollection.find({'genderPred': int(request.args['genderPred'])}, {'_id': False})

    # if no filter was set, all the documents will be shown
    else:
        profiles = db.ifcollection.find({}, {'_id': False})

    # Iterating and appending all the json documents, both for filtered result or without!
    for profile in profiles:
        json_doc = json.loads(dumps(profile, sort_keys=True, indent=4))
        json_docs.append(json_doc)

    # jsonify returns the uni-code view of this function
    return jsonify(results=json_docs)




# Setting up the rout to access JSON data based on a single ID
@application.route('/if/api/v1.0/profile/<string:profile_id>', methods=['GET'])

# This function returns an individual profile data based on the single value, i.e: ID
def get_profile(profile_id):

    # fetching only one specific row
    profile = db.ifcollection.find({'id': profile_id})

    # jsonify returns the uni-code view of this function
    return jsonify(result=profile)




# It keeps track of the namespaces and runs when code.
# '__name__' is the global variable, usually module's name
if __name__ == '__main__':
    application.run(host='0.0.0.0')



# custom error page handling
@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

