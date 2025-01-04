from get_func_bearer import get_resp
import json 
url = "https://webexapis.com/v1/meetings"
with open('key.json', 'r') as file:
    config=json.load(file)
    key=config["key"]
get_resp(url, key, 0)
