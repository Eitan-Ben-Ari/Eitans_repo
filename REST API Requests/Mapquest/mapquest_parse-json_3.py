import requests
import urllib.parse
import json

main_api = "https://www.mapquestapi.com/directions/v2/route?"

with open('config.json', 'r') as f:
    config=json.load(f)
    key = config['key']
n=0
while True:
    n+=1
    orig = input('Starting Location: ')
    dest = input('Destination: ')
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data=requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    print("URL: " + (url))

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
    if n>=3:
     break