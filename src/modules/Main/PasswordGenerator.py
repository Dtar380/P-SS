########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS
from string import printable
from random import choices

########################################
#####  CODE                        #####
########################################

#####  FUNCTIONS
def generatePassword(K = 12) -> str:
    usable_characters = printable.translate({ord(i): None for i in ' \t\n\r\x0b\x0c'})
    password = "".join(choices(usable_characters, k=K))
    return password

def main() -> None:
    password = generatePassword()
    print(password)

#####  RUN FILE
if __name__ == "__main__":
    main()