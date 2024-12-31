import requests
import urllib.parse
import json
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Roma, Italia"
dest = "Frascati, Italia"

with open('config.json', 'r') as f:
    config=json.load(f)
    key = config['key']

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data=requests.get(url).json()
json_status = json_data["info"]["statuscode"]

print("URL: " + (url))
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")