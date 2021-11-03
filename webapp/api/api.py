"""
website.py
Used to interact take a resouce and output
Author(s): Kale Satta-Hutton
Group: NASAK
CIS422 F21
Last Modifed Date: 11/3/21
Description:
    This file contains the compute class called with Resource call
    'http://restapi:5000/' + 'compute/' + DATA where data is a json.dumps
    dictionary with an array of googleapis place_id which will be run through
    a variety of functions to output the optimal path.
"""
# Streaming Service
from flask import Flask, jsonify  # Flask instantiates the flask app api.py, jsonify turns data into a json object
from flask_restful import Resource, Api  # Resource is what a class is called with, Api instantiates the Api depenendency
import jsons  #use loads to turn string form of data into an array of dicts
from geneticAlgorithm import *  # source code for genetic algorithm
from mapsAPI import *  # creates distance matrix from googlemapsapi


app = Flask(__name__)
api = Api(app)
app.config.from_object(__name__)


class compute(Resource):
    """
    flask_restful Resouce and Api class called by '/compute/<string:data>'
    """
    def get(self, data):
        """
        API called with get request with the proper json.dumps string data structure.
        This function creates an array of dictionarys which contain a place_id.
        That array is used to create a distance matrix of all of the selected locations
        The distance matrix is used by the genetic algorithm computes and outputs a sorted array of place_id's
        """
        vals = jsons.loads(data)  # turn string data into an array of dicts
        place_id_list =[]  # list to call genMatrix
        for val in vals:
            # iterate through each dict
            place_id_list.append(val.get('place_id'))  # put the place_id in the place_id_list
        dist_mtx, name_list = genMatrix(place_id_list)   #generate distance matrix
        population = parse_input((dist_mtx, name_list))  # creates city objects
        popSize = 100
        eliteSize = 50
        mutationRate = 0.05
        generations = 75
        sorted_place_id = geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations)
        # the array to be returned in order of optimal distance traveled.
        out =   {
                "ret": sorted_place_id
                }
        # dictionary of data to be returned.
        return jsonify(out)  # turn the dict into a json object.


# Create routes
api.add_resource(compute, '/compute/<string:data>')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
