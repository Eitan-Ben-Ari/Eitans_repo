import json
#מילון בפייתון
dic = {'name':'eitan','age':21, 'hobby':'playing the piano'}
#יוצר קובץ גייסון חדש שהוא התרגום של המילון
with open('my_serialize_json.json', 'w') as file:
 json.dump(dic, file)
