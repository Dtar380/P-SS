########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS


#####  INTERNAL IMPORTS


########################################
#####  CODE                        #####
########################################

#####  CLASS
class User:

    """
    Creates a User type object which contains the variables of:\n
     · Username: To store the username
     · Password: To store the password
     · Selected: Stores a boolean value that tells if user is selected ot not
    """

    def __init__(self, username: str, password: str, selected: bool = None):
        self.username = username # Gets the username argument of the User
        self.password = password # Gets the uuid argument of the User
        self.selected = selected # Gets the selected argument of the User
        self.key = None

    # Creates a dictionary with the parameters
    def user_dict(self):
        return {
            'User': self.username,
            'Password': self.password,
            'Selected': self.selected
        }

#####  RUN FILE
if __name__ == "__main__":
    pass