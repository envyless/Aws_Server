# This Python file uses the following encoding: utf-8

#########################################
#     python 2.7.3
#########################################

# command
# init_db
# deploy

import os
import sys

from database import init_db


if __name__ == "__main__":
    command = sys.argv[1]

    if command == "init_db":
        init_db()
    elif command == "deploy":
        os.system("pip freeze > requirement.txt")
        os.system("eb deploy")

    print "finished " + command
