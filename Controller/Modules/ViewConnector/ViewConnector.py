"""
this module provides functions to check if the request is valid,
parse the request in a usable format
"""

def validateRequest(req, needsKey = False):
    """checks the req.data, ensures it's valid json file(could easily converted to python dictionary), and has a "key" element"""
    #content = req.get_json()
    content = req
    isValid = True
    if ('key' not in content):
        print("request rejected: missing key")
        content['error'] = 'key'
        isValid = False
    elif ('username' not in content):
        print("request rejected: missing username")
        content['error'] = 'missing username'
        isValid = False
    if(needsKey):
        print('needs key')

    if(isValid):
        print("request is validated...")

    return isValid

def parseRequestData(req):
    """convert the json file into a dictionary (should only be 1 line of code to do so)"""

    return []