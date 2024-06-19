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

#####  FUNCTIONS
def main() -> None:
    pass

#####  RUN FILE
if __name__ == "__main__":
    main()