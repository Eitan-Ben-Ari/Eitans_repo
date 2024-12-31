import json
import requests
import urllib3
api_url = "https://192.168.168.2/restconf/data/ietf-interfaces:interfaces\
/interface=Loopback2"
headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }


with open('config.json', 'r') as r:
    config = json.load(r)
    a=config['us']
    b=config['pa']


yangConfig = \
{
 "ietf-interfaces:interface": {
 "name": "Loopback2",
 "description": "My second RESTCONF loopback",
 "type": "iana-if-type:softwareLoopback",
 "enabled": True,
 "ietf-ip:ipv4": {
 "address": [
 {
 "ip": "10.2.1.1",
 "netmask": "255.255.255.0"
 }
 ]
 },
 "ietf-ip:ipv6": {}
 }
}

resp = requests.put(api_url, data=(json.dumps(yangConfig)), auth=(a,b),
headers=headers, verify=False)



if(resp.status_code >= 200 and resp.status_code <= 299):
 print("STATUS OK: {}".format(resp.status_code))
else:
 print('Error. Status Code: {} \nError message:\
{}'.format(resp.status_code, resp.json()))