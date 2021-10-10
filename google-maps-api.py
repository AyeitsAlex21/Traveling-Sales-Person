"""
Source Code for Google Maps API, CIS422 FA21
Author(s): Niklaas Cotta
Last Edited: 10/09/21
Sources:
  List of APIs: https://console.cloud.google.com/google/maps-apis/new?project=celestial-brand-308820
  Distance Matrix Documentation: https://developers.google.com/maps/documentation/distance-matrix/start
"""
import requests

API_KEY = "API_KEY"  # hide this
url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&destinations=New%20York%20City%2C%20NY&units=imperial&key="
url += API_KEY

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)