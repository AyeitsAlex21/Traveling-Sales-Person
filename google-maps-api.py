"""
Source Code for Google Maps API, CIS422 FA21
Author(s): Niklaas Cotta
Last Edited: 10/09/21
Sources:
  List of APIs: https://developers.google.com/maps/documentation
  Distance Matrix Documentation: https://developers.google.com/maps/documentation/distance-matrix/start
"""
import requests


def get_distance(origins, destinations):
    """
    :param origins: list of addresses (strings)
    :param destinations: list of addresses (strings)
    :return: list of distances (ints)
    """
    API_KEY = ""  # need to hide this
    i = 1
    distances = []

    # base url
    for origin, destination in zip(origins, destinations):
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?" \
              f"origins={origin}&destinations={destination}" \
              f"&units=imperial&key={API_KEY}"

        # get request
        response = requests.request("GET", url, headers={}, data={})
        # print(response.text)
        output = response.json()
        distances.append(output["rows"][0]["elements"][0]["distance"]["text"])

        # formatted output (temp)
        print("Distance #", i)
        print("Place of Origin:  ", output["destination_addresses"][0])
        print("Destination:      ", output["origin_addresses"][0])
        print("Distance between: ", output["rows"][0]["elements"][0]["distance"]["text"])
        print("Time taken:       ", output["rows"][0]["elements"][0]["duration"]["text"])
        print("\n")


if __name__ == '__main__':
    # Example
    get_distance(["6128 Flag Point Drive, Ooltewah"], ["1710 E 15th Ave, Eugene"])
