import random
from Modules.DatabaseConnector import DatabaseConnector as db
from Modules.UserAuthenticator.Tracker import Tracker

"""
module responsible for ensuring that the user/pass is correct according to the database and deciding what
type of the user it is. It will also check the request's sender to make sure it is authorized.
"""

def userIsValid(user):
    result = False
    user_info = getUserInfo(user)
    if(('Passwd' in user_info) and ('password' in user) and user_info['Passwd'] == user['password']):
        result = True
        print(user['username'] + ' has correct passwd')
        user['type'] = user_info['Type_of_user']
    else:
        print(user['username'] + ' failed login due to invalid user/pass combo')
    return result

def getUserInfo(user):
    result = db.getData("*", "Login_Info", "Username = '" + user['username'] + "'")
    if(len(result) > 0):
        result = result[0]
    else:
        result = {}
    return result
"""
user = {'username': 'username_05', 'password': 'password_05'}
userIsValid(user)
user = {'username': 'username_05', 'password': 'password_06'}
userIsValid(user)
user = {'username': 'username_042', 'password': 'password_06'}
userIsValid(user)
"""
def userIsAuthorized(user, request):
    tr = Tracker.getInstance()
    if(not tr.userIsActive(user['key'])):
        print('user is not in the active user pool.')
        user['error'] = 'not active.'
        return False
    else:
        print('user is in active pool.')

    user_info = tr.getActiveUserInfo(user['key'])
    if(user['username'] != user_info['username']):
        print('username does not match the key!!!')
        user['error'] = 'username does not match the key!'
        return False

    if(user_info['type'] == 'client'):
        if(request == 'modifyProfile'):
            return True
        elif (request == 'getQuote'):
            return True
        elif (request == 'createInvoice'):
            return True
        elif (request == 'getInvoice'):
            return True
        elif (request == 'getAllUsers'):
            return True
        elif (request == 'getUsersOfType'):
            return True
    return False
"""
user = {'username': 'username_05', 'password': 'password_05', 'key': '123'}
userIsAuthorized(user, 'getQuote')
"""
def generateUserKey():
    key = ""
    for i in range(0, 256):
        key += chr(random.randint(0,255))
    return key
"""
generateUserKey();
"""