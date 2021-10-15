# Streaming Service
from flask import Flask, jsonify, request, abort, Response
from flask_restful import Resource, Api
import os
from itsdangerous import (TimedJSONWebSignatureSerializer \
                                  as Serializer, BadSignature, \
                                  SignatureExpired)




app = Flask(__name__)
api = Api(app)

SECRET_KEY = 'test1234@#$'

class compute(Resource):
    def post(self):
        return {}, 201


# Create routes
# Another way, without decorators
api.add_resource(compute, '/compute', '/Compute')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
