"""
Source Code for Google Maps API, CIS422 FA21
Author(s): Niklaas Cotta
Last Edited: 10/09/21
Sources:
  List of APIs: https://developers.google.com/maps/documentation
  Distance Matrix Documentation: https://developers.google.com/maps/documentation/distance-matrix/start
"""
import requests


def get_distance():
    API_KEY = ""  # hide this
    origin = "Washington%2C%20DC"
    dest = "New%20York%20City%2C%20NY"

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?" \
          f"origins={origin}&destinations={dest}" \
          f"&units=imperial&key={API_KEY}"

    response = requests.request("GET", url, headers={}, data={})
    # print(response.text)
    output = response.json()

    print("Place of Origin:  ", output["destination_addresses"][0])
    print("Destination:      ", output["origin_addresses"][0])
    print("Distance between: ", output["rows"][0]["elements"][0]["distance"]["text"])
    print("Time taken:       ", output["rows"][0]["elements"][0]["duration"]["text"])


if __name__ == '__main__':
    get_distance()
