import json
import requests
import time 
def get_resp(url, key, write_to_file):

    response=requests.get(url, headers={'Authorization': f'Bearer {key}'})

    if write_to_file>0:
        for num in range(0,write_to_file):
            with open(f'file_{num}.json', 'w') as file:
                    json.dump(response.json(), file, indent=2)
    else:
        print(json.dumps(response.json(), indent=2))

if __name__=='__main__':
     url=input('I need a URL ________')
     key=input('I NEED YOUR bearer key :D         ')
     write_to_file=int(input('GIVE INT - num of files.\n those who wish for a STRING should give 0 as input______'))
     get_resp(url,key,write_to_file)
