import os
from cryptography.fernet import Fernet 
files =  [file for file in os.listdir() if os.path.isfile(file)]
with open('../mykey', 'rb') as mykey:
        raw_key=mykey.read()
for file in files:
    with open(file,'rb') as myfile:
        encrypted_content=myfile.read()
    decrypted_content=Fernet(raw_key).decrypt(encrypted_content)
    with open(file, 'wb') as myfile:
        myfile.write(decrypted_content)
