import base64, hashlib
from cryptography.fernet import Fernet, InvalidToken

keys = [Fernet.generate_key(), Fernet.generate_key()]

text = "Hola soy Dtar".encode()

ciphered_text = Fernet(keys[1]).encrypt(text)

for key in keys:
    try:
        deciphered_text = Fernet(key).decrypt(ciphered_text)
    except InvalidToken:
        print("Invalid Token")
    else:
        print(deciphered_text)