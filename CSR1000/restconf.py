import requests
import json
uri = "https://192.168.168.2/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"
headers= {
    'accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}
myjson = '''
{
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet1",
        "description": "its my fucking interface",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.168.2",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {
            "address": [
                {
                    "ip": "2001:acad:db8::"
                }
            ]
        }
    }
}

'''
request=requests.put(uri, headers=headers,data=myjson, verify=False)
print(request.text)
