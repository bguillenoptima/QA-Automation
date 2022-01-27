import requests
import json
response = requests.get('https://rahulshettyacademy.com/maps/api/place/get/json', params={'key':'qaclick123', 'place_id':'152763a70c12dcf34819bec8b0bff388'},)

json_response = response.json()
print(json_response)
print(type(json_response))
print(response.headers)
assert response.headers['server'] == "Apache/2.4.18 (Ubuntu)"

