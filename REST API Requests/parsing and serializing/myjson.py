import json
import yaml
#קורא את קובץ היאמל
with open('serialized_into.yaml','r') as yaml_file:
#הופך את היאמל למילון בפייתון
    ouryaml=yaml.load(yaml_file, Loader=yaml.FullLoader)
# מדפיס את המילון
print(ouryaml)
#בעזרת השייטה של פורמט אני מכניס ערך בתוך ה"סטרינג הערך של המפתח אקסס_טוקן" 
print("the access token is {}".format(ouryaml['access_token']))
print('the token expires in {} seconds'.format(ouryaml['expires_in']))
print("\n\n")
#הופך את מילון הפייתון ל"גייסון" ומדפיס אותו
print(json.dumps(ouryaml, indent=1))





