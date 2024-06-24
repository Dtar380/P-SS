########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS
from time import sleep

from subprocess import Popen

from os import system as execute
from platform import system as sys

from urllib import error, request

########################################
#####  CODE                        #####
########################################

#####  CLASS
class SystemFunctions:

    """
    Class that contains functions system related, like:\n
     · Check OS Compatibility: Checks if OS is compatible with list of OS
     · Clear: Clears the console
    """

    compatible_os = ['Windows', 'Darwin', 'Linux']

    def __init__(self) -> None:
        self.os = sys()
        self.check_os_compatibility()

    def check_os_compatibility(self) -> None:
        if self.os in self.compatible_os:
            pass
        else:
            raise Exception('\nSystem not compatible\n')
            exit()

    def clear(self, time: float = 1):
        sleep(time)
        execute('cls' if self.os == 'Windows' else 'clear')

#####  RUN FILE
if __name__ == "__main__":
    pass