import requests
import urllib.parse
import json

main_api = "https://www.mapquestapi.com/directions/v2/route?"

with open('config.json', 'r') as f:     #opens the "config.json" file for READ 
    config=json.load(f)                 #load it to the system as a python dic
    key = config['key']                 #saves the value as a variable
n=0
while True:
    n+=1
    orig = input('Starting Location: ')
    dest = input('Destination: ')
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})    
    #url= converted dictionary into a URL query string + "main api"
    json_data=requests.get(url).json()     #parsed response saved to "json_data" variable
    json_status = json_data["info"]["statuscode"]

    print("URL: " + (url))

    if json_status == 0:        #just if successful!
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:" + (json_data["route"]["formattedTime"]))
        print("Miles:" + str(json_data["route"]["distance"]))
        print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("=============================================")
    if n>=3:
     break