import re
from Modules.DatabaseConnector import DatabaseConnector as db
from Modules.UserAuthenticator import UserAuthenticator as UA
"""
module responsible for registrating different types of users.
checking if the new email is not already in use, password is strong, etc.
"""
"""check the format of the email. it must be smth@smth.smth"""
def emailIsValid(email):
    if re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email):
        return True
    else:
        return True

"""check if the email is taken or not"""
def emailAvailable(email):
    user = UA.getUserInfo({'username': email})
    if(user):
        return False
    else:
        return True

def passwordIsValid(password):
    if password != "":
        return True
    return False

"""we could either use user,pass or User class to represent a user here"""
def registerClient(user):
    return False

def registerAgent(user):
    return False

def registerManager(user):
    return False

