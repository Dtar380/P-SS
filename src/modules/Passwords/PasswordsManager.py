########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS
from cryptography.fernet import Fernet, InvalidToken

from string import printable
from random import choices

from os.path import exists
from json import loads, dump

#####  INTERNAL IMPORTS
from modules.Passwords.Password import Password

########################################
#####  CODE                        #####
########################################

#####  CLASS
class PasswordManager:

    usable_characters = printable.translate({ord(i): None for i in ' \t\n\r\x0b\x0c'})

    def __init__(self, file: str, username: str, key: str) -> None:
        self.file = file
        self.username = username
        self.cipher = Fernet(key)
        self.passwords = self.checkPasswords()

    def checkPasswords(self) -> "list[Password]":
        if exists(self.file):
            passwords = self.readPasswords()
            return passwords
        
        else:
            raise Exception('Error. No password file detected.')

    def readPasswords(self) -> "list[Password]":
        with open(self.file, 'r') as f:
            data: dict = loads(f.read())
            keys = list(data.keys())
            f.close()
                
        for i, key in enumerate(keys):
            try:
                self.cipher.decrypt(key)
                passwords = data[key]
            except InvalidToken:
                pass

        return [Password(inst['Site'], inst['User'], inst['Password']) for inst in passwords]

    def createPassword(self) -> None:
        non_encrypted_site: str = input('Enter the name of the site: ')
        non_encrypted_username = input('Enter the username of the site: ')
        length = int(input('Enter length of the password: '))
        non_encrypted_password = self.generatePassword(length)

        site = self.cipher.encrypt(non_encrypted_site.encode()).decode()
        username = self.cipher.encrypt(non_encrypted_username.encode()).decode()
        password = self.cipher.encrypt(non_encrypted_password.encode()).decode()

        new_password: Password = Password(site, username, password)
        self.passwords.append(new_password)
        self.savePasswords()

    def generatePassword(self, K: int = 12) -> str:
        return "".join(choices(self.usable_characters, k=K))

    def deletePassword(self, password_id: int) -> None:
        if 0 <= password_id < len(self.passwords):
            del self.passwords[password_id]
        
        else:
            raise Exception('Password out of range')

        self.savePasswords()

    def savePasswords(self) -> None:
        with open(self.file, 'r') as f:
            data: dict = loads(f.read())
            f.close()
        
        key = self.cipher.encrypt(self.username.encode()).decode()
        data[key] = [inst.password_dict() for inst in self.passwords]

        with open(self.file, 'w') as f:
            dump(data, f, indent=4, separators=(',',':'))
            f.close()

    def peekPassword(self, password_id) -> str:
        encrypted_password: str = self.passwords[password_id]
        password = self.cipher.decrypt(encrypted_password.encode()).decode()
        return password

#####  RUN FILE
if __name__ == "__main__":
    pass