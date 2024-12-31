import json
import requests
import urllib3
urllib3.disable_warnings()
uri = "https://192.168.168.2/restconf/data/ietf-interfaces:interfaces/"

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"}

with open('config.json', 'r') as r:
    config = json.load(r)
    a=config['us']
    b=config['pa']

resp = requests.get(uri, auth=(a,b), headers=headers, verify=False)
response_parsed=resp.json()
print(json.dumps(response_parsed, indent=4))
