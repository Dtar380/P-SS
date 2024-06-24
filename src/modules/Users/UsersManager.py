########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS
from cryptography.fernet import Fernet
import base64, hashlib

from os.path import exists
from json import loads, dump

#####  INTERNAL IMPORTS
from modules.Users.User import User
from modules.System.Colors import cPrint

########################################
#####  CODE                        #####
########################################

#####  CLASS
class UsersManager:

    """
    Manages all Users and actions related to them such as:\n
     · Reading: Reads from the users file all users
     · Creating: Creates a new user given a username and a password
     · Deleting: Deletes the specified non-selected user
     · Saving: Saves the usernames and passwords to an encrypted file
     · Select: Selects the specified non-selected user
    """

    def __init__(self, file: str) -> None:
        self.file = file
        self.users = self.checkUsers()
        if not self.users: self.createUser(True)

    def checkUsers(self) -> "list[User]":
        if exists(self.file):
            users = self.readUsers()
            return users

        else:
            raise Exception('Error. No users file detected.')
        
    def readUsers(self) -> "list[User]":
        with open(self.file, 'r') as f:
            data: list = loads(f.read())
            f.close()

        return [User(inst['User'], inst['Password'], inst['Selected']) for inst in data]

    def createUser(self, selected: bool = None) -> None:
        username = input('Enter a username: ')
        input_password = input('Enter a password: ').encode()

        key = base64.urlsafe_b64encode(
            hashlib.md5(input_password).hexdigest().encode()
        )

        password = Fernet(key).encrypt(input_password).decode()

        new_user: User = User(username, password, selected)
        self.users.append(new_user)
        self.saveUsers()

    def deleteUser(self, user_id: int) -> None:
        if 0 <= user_id < len(self.users):
            if self.users[user_id].selected:
                raise Exception('User is selected.')
            
            else:
                del self.users[user_id] # Deletes the user

        else:
            raise Exception('User out of range')
                
        self.saveUsers() # Saves the users into the json

    def saveUsers(self) -> None:
        data = [inst.user_dict() for inst in self.users]

        with open(self.file, 'w') as f:
            dump(data, f, indent=4, separators=(',',':'))
            f.close()

    def selectUser(self, user_id: int) -> None:
        if 0 <= user_id < len(self.users):
            for inst in self.users:
                inst.selected = False

            if self.checkPassword(user_id):

                self.users[user_id].selected = True
                self.saveUsers

    def checkPassword(self, user_id: int) -> bool:
        encrypted_password = self.users[user_id].password
        input_password = input('Enter a password: ').encode()

        key = base64.urlsafe_b64encode(
            hashlib.md5(input_password).hexdigest().encode()
        )

        password = Fernet(key).decrypt(encrypted_password).decode()

        if password == input_password:
            self.users[user_id].key = key
            return True
        
        else:
            return False

    def getSelectedUser(self) -> list:
        for i in self.users:
            if i.selected:
                return [i.username, i.password]

UsersManager

#####  RUN FILE
if __name__ == "__main__":
    pass