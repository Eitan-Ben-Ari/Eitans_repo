import requests
uri = "https://netacad.com"
req1=requests.get(uri, headers={'accept': 'application/json'})
with open('file.html','w') as file:
    file.write(f'{req1.content}')

