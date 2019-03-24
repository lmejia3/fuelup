from Modules.UserAuthenticator import UserAuthenticator as UA
from Modules.UserAuthenticator.Tracker import Tracker
"""
module provides lot of functionalities required by the users. I intend to put all the use cases for the
usres as functions in this module. we would also create a excel file that specifies what type of user
has access to which functions, so it is easy it specify and modify user access to the functions.
"""

def login(user):
    response = {}
    isValid = UA.userIsValid(user)
    if(isValid):
        print(user['type'])
        key = UA.generateUserKey()
        user['key'] = key
        tracker = Tracker.getInstance()
        tracker.addUser(user)
        print(user['username'] + " successfully logged in")
        response['key'] = key
    else:
        print("user/pass did not match")
        response['error'] = "user/pass did not match"
    return response

def registerUser(user):
    return False

def modifyProfile(user, form):
    return False

def processOrder(user, order):
    return False

def getQuote(form):
    return 0.0

def setUser(user):
    return False

def unregisterUser(user):
    return False

def removeUser(user):
    return False

def getTransactionHistory(user, bounds):
    return ""

def getAllTransactionHistory(user):
    return ""

def getInvoices(user, bounds):
    return ""

def getCurrentEvent():
    return ""

def getRequestList():
    return ""

def getTrends(bounds):
    return ""

def getAllUsers():
    return ""

def getUsersOfType(type):
    return ""

def getProfitMargin(type):
    return 0.0

def setProfitMargin():
    return False