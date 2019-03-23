import random
from Modules.DatabaseConnector import DatabaseConnector as db
"""
module responsible for ensuring that the user/pass is correct according to the database and deciding what
type of the user it is. It will also check the request's sender to make sure it is authorized.
"""

def userIsValid(user):
    result = False
    user_info = getUserInfo(user)
    if(user_info['Passwd'] == user['password']):
        result = True
        print(user['username'] + ' has correct passwd')
    else:
        print(user['username'] + ' failed loggin due to invalid user/pass combo')
    user['type'] = user_info['Type_of_user']
    print("asdfzxcv")
    return result

def getUserInfo(user):
    result = db.getData("*", "Login_Info", "Username = '" + user['username'] + "'")
    result = result[0]
    return result

def userIsAuthorized(user, request):
    return False

def generateUserKey():
    key = ""
    for i in range(0, 256):
        key += chr(random.randint(0,255))
    return key
