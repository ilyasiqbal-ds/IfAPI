__author__ = 'Ilyas'


import json
from flask import Flask, jsonify, request
from flask import make_response
from flask import abort
from bson import Binary, Code, ObjectId
from bson.json_util import dumps
import Config


app = Flask(__name__)


db = Config.dbConnect()


@app.route('/if/api/v1.0/profile', methods=['GET'])
def get_profiles():

    json_docs = []
    if 'numSales' in request.args:
        profiles = db.ifcollection.find({'numSales': request.args['numSales']}, {'_id': False})
    elif 'genderPred' in request.args:
        profiles = db.ifcollection.find({'genderPred': int(request.args['genderPred'])}, {'_id': False})
    else:
        profiles = db.ifcollection.find({}, {'_id': False})

    for profile in profiles:
        json_doc = json.loads(dumps(profile, sort_keys=True, indent=4))
        json_docs.append(json_doc)
    return jsonify(results=json_docs)



@app.route('/if/api/v1.0/profile/<string:profile_id>', methods=['GET'])
def get_profile(profile_id):

    profile = db.ifcollection.find({'id': profile_id})
    json_doc = json.loads(dumps(profile, sort_keys=True, indent=4))
    return jsonify(result=json_doc)


if __name__ == '__main__':
    app.run(debug=True)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

