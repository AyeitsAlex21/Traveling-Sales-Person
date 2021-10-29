"""
mapsAPI.py
Source Code for Google Maps API or interaction between genetic algorithm and google maps
Author(s): Niklaas Cotta
CIS422 FA21
Creation Date: 10/9/21
Sources:
  List of APIs: https://developers.google.com/maps/documentation
  Distance Matrix Documentation: https://developers.google.com/maps/documentation/distance-matrix/start
Description:
  This file contains two functions. The first function, get_distance() contains the distance API call to google maps.
  The second function, genMatrix(), creates a complete graph containing n addresses as vertices. This graph is in matrix
  form. For each vertex (address) pair, calculates the distance between the two.
"""
import requests  # this library is how python makes requests to APIs
import regex     # this library is for parsing strings with regular expressions


def get_distance(origin, destination):
    """
    This function takes a source string and a destination string in the form of an address.
    Address may be in following forms:
        1710 E 15th Ave, OR
        6513 Flag Way Dr, Boise, Idaho
        Seattle, Washington
        San Francisco, CA
    Function then requests distance between source and destination from google maps API.
    If successful request, gets the distance from the json, and converts the distance from a string to integer
    On failure returns -1. On success returns distance between the two places.
    :param origin: str
    :param destination: str
    :return: float (distance between the two)
    """

    # get API key
    fp = open("api-key.txt", "r")  # open file containing api key
    API_KEY = fp.read()
    fp.close()

    # base url, used later in request to google
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?" \
          f"origins={origin}&destinations={destination}" \
          f"&units=imperial&key={API_KEY}"

    response = requests.request("GET", url, headers={}, data={})  # query response from maps, this is the API call
    if response.status_code != 200:  # 200 means OK
        print("Could not get distance from API")
        return -1

    response = response.json()  # convert response into json format
    distancestr = response["rows"][0]["elements"][0]["distance"]["text"]  # isolate .json element

    # this just turns the string into a float number
    found = regex.search(r"\d*[,.]*\d*", distancestr)
    distance = float(found.group().replace(",", ""))

    return distance  # float

########################################################################################################################


def genMatrix(addressList):
    """
    This function takes a list of addresses (strings) and generates a complete graph of distances between addresses.
    This graph is in the form of a matrix where each index corresponds to an address, in the order of addressList.
    After initially populating the matrix with 0s, the graph then calls get_distance() between each pair of addresses.
    The graph is undirected, so the matrix will have symmetry.
    :param addressList: list of str
    :return: tuple containing list of list of distances (matrix) and list of addresses (strings)
    """
    matrix = []  # empty var to be filled
    n = len(addressList)  # get length

    # populate initial matrix with 0's (n x n matrix)
    for j in range(n):
        matrix.append([])  # add a "row"
        for _ in range(n):
            matrix[j].append(0)

    for j in range(n):
        for i in range(n):
            if i != j:  # distance from x to x is 0
                distance = get_distance(addressList[i], addressList[j])  # api call
                matrix[j][i] = distance  # insert distance

    if any(-1 in row for row in matrix):  # make sure there are no invalid distances
        print("WARNING: Distance matrix contains invalid distance (-1). API function could not grab distance. Program will continue")

    return matrix, addressList  # returns tuple containing address list and corresponding matrix

########################################################################################################################


if __name__ == '__main__':
    # Example
    newAddresses = ["NYC, NY", "1710 E 15th Ave, Eugene,OR", "Cocoa Beach,FL", "Seattle, Washington"]
    newMatrix, addresses = genMatrix(newAddresses)

    for address in newMatrix:
        print(address)
