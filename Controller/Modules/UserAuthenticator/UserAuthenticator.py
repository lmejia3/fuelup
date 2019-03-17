import random
"""
module responsible for ensuring that the user/pass is correct according to the database and deciding what
type of the user it is. It will also check the request's sender to make sure it is authorized.
"""

def userIsValid(user):
    return False

def getUserType(user):
    return ""

def userIsAuthorized(user, request):
    return False

def generateUserKey():
    key = ""
    for i in range(0, 256):
        key += chr(random.randint(0,256))
    return key