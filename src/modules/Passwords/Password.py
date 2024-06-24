########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS


#####  INTERNAL IMPORTS


########################################
#####  CODE                        #####
########################################

#####  GLOBAL VARIABLES


#####  CLASS
class Password:

    def __init__(self, site: str, username: str, password: str) -> None:
        self.site = site
        self.username = username
        self.password = password

    def password_dict(self):
        return {
            'Site': self.site,
            'User': self.username,
            'Password': self.password
        }

#####  RUN FILE
if __name__ == "__main__":
    pass