import requests
import json

url = "https://192.168.168.2/restconf/data/ietf-interfaces:interfaces/interface=Loopback1"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback1",
    "description": "My first RESTCONF loopback",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "10.1.1.1",
          "netmask": "255.255.255.0"
        }
      ]
    },
    "ietf-ip:ipv6": {}
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
}


with open('config.json', 'r') as r:
    config = json.load(r)
    a=config['us']
    b=config['pa']


response = requests.request("PUT",url,auth=(a,b), headers=headers, data=payload, verify= False)

print(response.text)
print(response.status_code)
