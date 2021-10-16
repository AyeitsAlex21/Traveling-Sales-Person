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
    :param origin: str
    :param destination: str
    :return: int (distance between the two)
    """
    API_KEY = ""  # need to hide this

    # base url
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?" \
          f"origins={origin}&destinations={destination}" \
          f"&units=imperial&key={API_KEY}"

    response = requests.request("GET", url, headers={}, data={}).json()  # query response from google maps
    distancestr = response["rows"][0]["elements"][0]["distance"]["text"]  # isolate .json element

    # this just turns the string into integer form
    found = re.search(r"\d*,*\d*", distancestr)
    distance = int(found.group().replace(",", ""))

    return distance


def genMatrix(addressList):
    """
    :param addressList: a list of addresses, first is origin
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
        for i in range(n):
            if i != j:  # distance from x to x is 0
                distance = get_distance(addressList[i], addressList[j])

                matrix[i][j] = distance
                matrix[j][i] = distance  # undirected graph

        # print(matrix[j])
    # print(addressList)

    return addressList, matrix  # returns tuple containing address list and corresponding matrix


if __name__ == '__main__':
    # Example
    addresses, addressMat = genMatrix(["NYC, NY", "1710 E 15th Ave, Eugene,OR", "Cocoa Beach,FL", "Seattle, Washington"])
