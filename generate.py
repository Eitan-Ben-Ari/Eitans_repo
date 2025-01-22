from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
with open('mykey', 'wb') as the_key:
    the_key.write(key)