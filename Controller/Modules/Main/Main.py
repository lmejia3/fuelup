from Modules.UserAuthenticator import UserAuthenticator as UA
from Modules.UserRegistrator import UserRegistrator as UR
from Modules.DatabaseConnector import DatabaseConnector as db
from Modules.Pricing import Pricing as PR
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
        response['id'] = user['id']
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
    id = db.runQuery('SELECT Username_ID FROM Login_Info WHERE Username = "%s"' \
                     % (user['username']))[0]['Username_ID']
    db.runInsertQuery('INSERT INTO Profile_for_Users (Username_ID) VALUES (%s)' \
                      % (id))
    response['status'] = 'added'
    return response

"""
user = {'username': 'hello@hi.com', 'password': 'oioi'}
registerUser(user)
user = {'password': 'oioi'}
registerUser(user)
user = {'username': 'hello@hi.com', 'password': ''}
registerUser(user)
user = {'username': 'username_01', 'password': 'oioi'}
registerUser(user)
user = {'username': 'username_43', 'password': 'oioi'}
registerUser(user)
user = {'username': 'username_41', 'password': 'oioi'}
registerUser(user)
user = {'username': 'blah@hi.com', 'password': 'oioi'}
registerUser(user)
user = {'username': 'blah@hi.com', 'password': 'oioi'}
registerUser(user)
user = {'username': 'blah@hi.com', 'password': 'oioi'}
registerUser(user)
login(user)
"""

def modifyProfile(form):
    response = {}
    if('username' not in form or 'lastname' not in form, 'company' not in form, 'address1' not in form, 'address2' not in form, \
       'city' not in form, 'state' not in form, 'zipcode' not in form, 'firstname' not in form):
        print('field missing.')
        response['error'] = "field missing."
        return response
    q = 'SELECT * FROM Profile_for_Users INNER JOIN Login_Info ON Profile_for_Users.Username_ID = Login_Info.Username_ID WHERE Username = "%s"' \
        % (form['username'])
    curProfile = db.runQuery(q)
    print(len(curProfile))
    if(len(curProfile) == 0):
        id = db.runQuery('SELECT Username_ID FROM Login_Info WHERE Username = "%s"' \
            % (form['username']))[0]['Username_ID']
        db.runInsertQuery('INSERT INTO Profile_for_Users (Username_ID) VALUES (%s)' \
                          % (id))
    q = 'UPDATE Profile_for_Users NATURAL JOIN Login_Info SET First_Name = "%s", Last_Name = "%s", Company_Name = "%s", Address = "%s", City = "%s", State = "%s", Zipcode = %s WHERE Username = "%s";' \
        % (form['firstname'], form['lastname'], form['company'], form['address1'] + form['address2'], form['city'], form['state'], form['zipcode'], form['username'])
    db.runInsertQuery(q)
    response['status'] = 'updated'
    return response

def getProfile(form):
    response = {}
    q = 'SELECT * FROM Profile_for_Users WHERE Username_ID = "%s"' \
        % (form['id'])
    curProfile = db.runQuery(q)
    return curProfile

print(getProfile({'id' : 1}))

def processOrder(user, order):
    return False

def getQuote(form):
    response = {}
    if ('gallons' not in form or 'date' not in form or 'username' not in form):
        print('field missing')
        response['error'] = 'field missing'
        return response

    price = PR.getQuote(form)
    today = str(date.today())

    response['price'] = price
    response['today'] = today
    response['price'] = form['price']
    response['history'] = form['history']
    response['season'] = form['season']
    response['location'] = form['location']
    response['amount'] = form['amount']
    response['profit'] = form['profit']
    response['rate'] = form['rate']

    db.runInsertQuery('INSERT INTO Quote (Username_ID, Number_of_Gallons, Price, Request_Date, Request_Delivery_Date) VALUES (%s, %s, %s, "%s", "%s")' \
                     % (form['id'], form['gallons'], price, today, form['date']))

    return response

def createInvoice(form):
    response = {}
    if ('quote_id' not in form or 'username' not in form):
        print('field missing')
        response['error'] = 'field missing'
        return response

    q = 'INSERT INTO Invoice'

    return response
"""
form = {'quote_id' : '1', 'username': 'us'}
createInvoice(form)
form = {'quote_id' : '1'}
createInvoice(form)
"""
def getInvoices(user):
    response = {}
    if ('username' not in user):
        print('field missing')
        response['error'] = 'field missing'
        return response

    q = 'SELECT Number_of_Gallons, Price, Request_Delivery_Date, Delivery_Date, Paid FROM Invoice, Quote WHERE Invoice.Username_ID = "%s" AND Invoice.Username_ID = Quote.Username_ID' \
        % (user['id'])
    result = db.runQuery(q)
    return result

def getAllUsers():
    response = {}
    q = 'SELECT * FROM Login_Info INNER JOIN Profile_for_Users ON Login_Info.Username_ID = Profile_for_Users.Username_ID'
    result = db.runQuery(q)
    dataobj = {}
    for i in range(0, len(result)):
        dataobj[i] = result[i]
    response['invoices'] = dataobj;
    return response
"""
getAllUsers()
"""
def getUsersOfType(t):
    response = {}
    if (type(t) != type("str")):
        print('type is not string.')
        response['error'] = 'type is not string'
        return response

    q = 'SELECT * FROM Login_Info INNER JOIN Profile_for_Users ON Login_Info.Username_ID = Profile_for_Users.Username_ID WHERE Login_Info.Type_of_user = "%s"' \
        % (t)
    result = db.runQuery(q)
    dataobj = {}
    for i in range(0, len(result)):
        dataobj[i] = result[i]
    response['invoices'] = dataobj;
    return response

def getQuoteHistory(user):
    response = {}
    if ('username' not in user or 'id' not in user):
        print('field missing')
        response['error'] = 'field missing'
        return response

    q = 'SELECT * FROM Quote WHERE Username_ID = "%s"' \
        % (user['id'])
    result = db.runQuery(q)
    for i in range(0, len(result)):
        result[i]['Price'] = float (result[i]['Price'])
    return result

print(getQuoteHistory({'username': '1', 'id':1}))

def getCurrentEvent():
    return ""
"""
getCurrentEvent()
"""
def getRequestList():
    return ""
"""
getRequestList()
"""
def getTrends(bounds):
    return ""
"""
getTrends(1)
"""
def getProfitMargin(type):
    return 0.0
"""
getProfitMargin(1)
"""

def setProfitMargin():
    return False
"""
setProfitMargin()
"""
def setUser(user):

    return False
"""
setUser(1)
"""
def unregisterUser(user):
    return False
"""
unregisterUser(1)
"""
def removeUser(user):
    return False
"""
removeUser(1)
"""
def getTransactionHistory(user, bounds):
    return ""
"""
getTransactionHistory(1,1)
"""
def getAllTransactionHistory(user):
    return ""
"""
getAllTransactionHistory(1)
"""