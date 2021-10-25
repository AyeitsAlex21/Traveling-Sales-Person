# Streaming Service
from flask import Flask, jsonify, request, abort, Response
from flask_restful import Resource, Api
import os
import jsons
from itsdangerous import (TimedJSONWebSignatureSerializer \
                                  as Serializer, BadSignature, \
                                  SignatureExpired)
from main import *


app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__)


class compute(Resource):
    def get(self, data):
        app.logger.debug(data)
        app.logger.debug("request.args: {}".format(request.args))
        vals = jsons.loads(data)
        app.logger.debug("Got vals")
        app.logger.debug(type(vals))
        app.logger.debug(vals)
        place_id_list =[]
        for val in vals:
            app.logger.debug(type(val))
            app.logger.debug(val)
            place_id_list.append(val.get('place_id'))
        dist_mtx, name_list = genMatrix(place_id_list)
        for name in name_list:
            app.logger.debug(name)
        population = parse_input((dist_mtx, name_list))
        popSize = 100
        eliteSize = 50
        mutationRate = 0.05
        generations = 300
        sorted_place_id = geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)
        for place in sorted_place_id:
            app.logger.debug(type(place))
            app.logger.debug(place)
        out =   {
                "ret": sorted_place_id
                }
        return jsonify(out)
        #return jsons.dumps(out)#flask.jsonify(out=out), 200


# Create routes
# Another way, without decorators
api.add_resource(compute, '/compute/<string:data>')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
