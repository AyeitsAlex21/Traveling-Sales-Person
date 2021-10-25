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
        dist_mtx, name_list = genMatrix(vals)
        population = parse_input((dist_mtx, name_list))
        popSize = 100
        eliteSize = 50
        mutationRate = 0.05
        generations = 300
        vals = geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)
        return jsonify(vals), 200


# Create routes
# Another way, without decorators
api.add_resource(compute, '/compute/<string:data>')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
