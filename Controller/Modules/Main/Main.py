from Modules.UserAuthenticator import UserAuthenticator as UA
from Modules.UserRegistrator import UserRegistrator as UR
from Modules.DatabaseConnector import DatabaseConnector as db
from datetime import date
from Modules.UserAuthenticator.Tracker import Tracker
"""
module provides lots of functionalities required by the users. I intend to put all the use cases for the
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
        response['key'] = key
        response['type'] = user['type']
        tracker = Tracker.getInstance()
        tracker.addUser(user)
        print(user['username'] + " successfully logged in")
    else:
        print("user/pass did not match")
        response['error'] = "user/pass did not match"
    return response

def registerUser(user):
    response = {}
    if(('username' not in user) or ('password' not in user)):
        print('user or pass is missing for registration')
        response['error'] = 'user/pass missing'
        return response
    elif(not UR.emailIsValid(user['username'])):
        print('email format is wrong.')
        response['error'] = 'wrong email format'
        return response
    elif(not UR.passwordIsValid(user['password'])):
        print('password is too weak.')
        response['error'] = 'password is weak'
        return response
    elif(not UR.emailAvailable(user['username'])):
        print('email is taken.')
        response['error'] = 'email is taken'
        return response

    user['type'] = 'client'
    user['date'] = str(date.today())
    q = 'INSERT INTO Login_Info (Username, Passwd, Type_of_user, Register_Date) VALUES ("%s", "%s", "%s", "%s");' \
        % (user['username'], user['password'], user['type'], user['date'])
    db.runInsertQuery(q)
    response['status'] = 'added'
    return response

def modifyProfile(form):
    response = {}
    q = 'UPDATE Profile_for_Users NATURAL JOIN Login_Info SET First_Name = "%s", Last_Name = "%s", Company_Name = "%s", Address = "%s", City = "%s", State = "%s", Zipcode = %s WHERE Username = "%s";' \
        % (form['firstname'], form['lastname'], form['company'], form['address1'], form['city'], form['state'], form['zipcode'], form['username'])
    db.runInsertQuery(q)
    response['status'] = 'updated'
    return response


form = {'firstname': 'ftest_001', 'lastname': 'ltest_001', 'company': 'ctest_001', 'address1': 'address1', 'address2': 'address2', 'city': 'katy', 'state': 'GG', 'zipcode': '12345', 'username': 'username_07'}
q = 'UPDATE Profile_for_Users NATURAL JOIN Login_Info SET First_Name = "%s", Last_Name = "%s", Company_Name = "%s", Address = "%s", City = "%s", State = "%s", Zipcode = %s WHERE Username = "%s";' \
    % (form['firstname'], form['lastname'], form['company'], form['address1'], form['city'], form['state'], form['zipcode'], form['username'])
modifyProfile(form)

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