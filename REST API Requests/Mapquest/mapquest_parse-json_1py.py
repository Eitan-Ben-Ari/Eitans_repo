import requests
import urllib.parse
import json
import yaml
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Natanya, ISRAEL"
dest = "Rishon Letsiyon, ISRAEL"
with open('config.json', 'r') as f:
    config=json.load(f)
    key = config['key']
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data=requests.get(url).json()
file=json.dumps(json_data, indent=2, ensure_ascii=False )
print(file)