import json
import myfile2
with open('new_file.json','r') as json_file:
    dic=json.load(json_file)
with open('myfile2.py','w') as py_file:
    py_file.write(f'{dic}')