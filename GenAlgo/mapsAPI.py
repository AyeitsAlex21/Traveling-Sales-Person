"""
Source Code for Google Maps API, CIS422 FA21
Author(s): Niklaas Cotta
Last Edited: 10/16/21
Sources:
  List of APIs: https://developers.google.com/maps/documentation
  Distance Matrix Documentation: https://developers.google.com/maps/documentation/distance-matrix/start
"""
import requests
import re


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
    :return: int (distance between the two)
    """

    # get API key
    fp = open("api-key.txt", "r")
    API_KEY = fp.read()
    fp.close()

    # base url
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?" \
          f"origins={origin}&destinations={destination}" \
          f"&units=imperial&key={API_KEY}"

    response = requests.request("GET", url, headers={}, data={})  # query response from google maps
    if response.status_code != 200:
        print("Could not get distance from API")
        return -1

    response = response.json()
    distancestr = response["rows"][0]["elements"][0]["distance"]["text"]  # isolate .json element

    # this just turns the string into integer form
    found = re.search(r"\d*,*\d*", distancestr)
    distance = int(found.group().replace(",", ""))

    return distance  # integer


def genMatrix(addressList):
    """
    This function takes a list of addresses (strings) and generates a complete graph of distances between addresses.
    This graph is in the form of a matrix where each index corresponds to an address, in the order of addressList.
    After initially populating the matrix with 0s, the graph then calls get_distance() between each pair of addresses.
    The graph is undirected, so the matrix will have symmetry.

    :param addressList: list of str
    :return: tuple containing list of list of distances (matrix) and list of addresses (strings)
    """
    matrix = []
    n = len(addressList)

    # populate initial matrix
    for j in range(n):
        matrix.append([])
        for _ in range(n):
            matrix[j].append(0)

    for j in range(n):
        for i in range(j, n):  # we consider distance same in both directions, reduces request waiting time
            if i != j:  # distance from x to x is 0
                distance = get_distance(addressList[i], addressList[j])

                matrix[i][j] = distance
                matrix[j][i] = distance  # distances are same

    if any(-1 in row for row in matrix):
        print("WARNING: Distance matrix contains invalid distance (-1). API function could not grab distance. Program will continue")

    return matrix, addressList  # returns tuple containing address list and corresponding matrix


if __name__ == '__main__':
    # Example
    newAddresses = ["NYC, NY", "1710 E 15th Ave, Eugene,OR", "Cocoa Beach,FL", "Seattle, Washington"]
    newMatrix, addresses = genMatrix(newAddresses)

    for address in newMatrix:
        print(address)
