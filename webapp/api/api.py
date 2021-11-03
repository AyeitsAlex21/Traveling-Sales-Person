"""
api.py
Source Code restful service that computes given a resource.
Author(s): Kale Satta-Hutton
CIS422 F21
Last Modifed Date: 10/31/21
Description:
  This file contains the compute class that takes a Resource call
  'http://restapi:5000/' + 'compute/' + DATA
  where the DATA is a json structure of googleapis place_id which will then be
  ran through a variety of functions to output the optimal path.

"""from flask import Flask, jsonify, request, abort, Response
from flask_restful import Resource, Api
import os
from itsdangerous import (TimedJSONWebSignatureSerializer \
                                  as Serializer, BadSignature, \
                                  SignatureExpired)
from geneticAlgorithm import *


app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__)


class compute(Resource):
    """
    
    """
    def get(self, data):
        """
        """
        vals = jsons.loads(data)
        place_id_list =[]
        for val in vals:
            place_id_list.append(val.get('place_id'))
        dist_mtx, name_list = genMatrix(place_id_list)
        population = parse_input((dist_mtx, name_list))
        popSize = 100
        eliteSize = 50
        mutationRate = 0.05
        generations = 75
        sorted_place_id = geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)
        out =   {
                "ret": sorted_place_id
                }
        return jsonify(out)


# Create routes
# Another way, without decorators
api.add_resource(compute, '/compute/<string:data>')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
