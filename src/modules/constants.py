########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS
from os.path import join
from os import environ as env

########################################
#####  CODE                        #####
########################################

#####  GLOBAL VARIABLES
application_path, application_files_path = join(env['APPDATA'], '.PASS')
files = ['passwords.json', 'users.json']