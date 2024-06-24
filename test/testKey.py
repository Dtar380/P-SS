from cryptography.fernet import Fernet
import base64, hashlib

input_password = input('Enter a password: ').encode()

key = base64.urlsafe_b64encode(
    hashlib.md5(input_password).hexdigest().encode()
)

cipher = Fernet(key)

encrypted_password = cipher.encrypt(input_password).decode()
password = cipher.decrypt(encrypted_password).decode()

print(f"""
Input password {input_password}
Encrypted password {encrypted_password}
Password {password}
""")