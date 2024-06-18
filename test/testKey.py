import base64, hashlib
from cryptography.fernet import Fernet

ciphered = b'gAAAAABmcNrSO8A2iIDMPHDvpoR4x1iO-Hvq7pYTK-5HCuuOHmzVP7MadlAEqUpZz4YYFo5n2qSWMO-1ww_KQb09pwGb2zVOwA=='

input_password = input('Enter a password: ').encode()

key = base64.urlsafe_b64encode(
    hashlib.md5(input_password).hexdigest().encode()
)

deciphered = Fernet(key).decrypt(ciphered).decode()

if deciphered == input_password.decode():
    print("SUCCESS")