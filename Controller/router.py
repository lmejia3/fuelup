from flask import Flask, request
from flask_cors import CORS, cross_origin
from Modules.ViewConnector import ViewConnector as vc
from Modules.Main import Main
from Modules.UserAuthenticator.Tracker import Tracker
from Modules.UserAuthenticator import UserAuthenticator as ua
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

"""
in the router module, we simply forward the coming requests to the python application.
we need to verify each request, ensuring: the user has privilege to use the requested function,
the format of the request is appropriate, and only then, call the requested function.
"""

Tracker() #initializing the singleton class

#user = {'username': 'username_09', 'password': 'password_09', 'key': '123'} #for testing

@app.route('/')
def dosmth():
    print("request @default arrived...")
    return 'successfully received the request'

@app.route('/function/login', methods=['POST', 'GET'])
def login_route():
    print("request @login arrived...")
    content = request.get_json() #replace user with content
    response = {}
    if(vc.validateRequest(content)):
        response = Main.login(content)
    if('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)

@app.route('/function/registerUser', methods=['POST', 'GET'])
def registerUser_route():
    print("request @registerUser arrived...")
    content = request.get_json()
    response = {}
    if(vc.validateRequest(content)):
        response = Main.registerUser(content)
    if('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)

@app.route('/function/modifyProfile', methods=['POST', 'GET'])
def modifyProfile_route():
    print("request @modifyProfile arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getQuote')):
        response = Main.modifyProfile(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)

@app.route('/function/processOrder', methods=['POST', 'GET'])
def processOrder_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to processOrder'

@app.route('/function/getQuote', methods=['POST', 'GET'])
def getQuote_route():
    print("request @getQuote arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getQuote')):
        response = Main.getQuote(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)

@app.route('/function/createInvoice', methods=['POST', 'GET'])
def createInvoice_route():
    print("request @createInvoice arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'createInvoice')):
        response = Main.createInvoice(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response, default=str)
    return json.dumps(response, default=str)

@app.route('/function/getProfile', methods=['POST', 'GET'])
def getProfile_route():
    print("request @getProfile arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getProfile')):
        response = Main.getProfile(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)

@app.route('/function/setUser', methods=['POST', 'GET'])
def setUser_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to setUser'

@app.route('/function/unregisterUser', methods=['POST', 'GET'])
def unregisterUser_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to unregisterUser'

@app.route('/function/removeUser', methods=['POST', 'GET'])
def removeUser_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to removeUser'

@app.route('/function/getTransactionHistory', methods=['POST', 'GET'])
def getTransactionHistory_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getTransactionHistory'

@app.route('/function/getAllTransactionHistory', methods=['POST', 'GET'])
def getAllTransactionHistory_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getAllTransactionHistory'


@app.route('/function/getInvoices', methods=['POST', 'GET'])
def getInvoices_route():
        print("request @getInvoices arrived...")
        content = request.get_json()
        response = {}
        if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getInvoices')):
            response = Main.getInvoices(content)
        if ('error' in content):
            response['error'] = content['error']
            return json.dumps(response, default=str)
        return json.dumps(response, default=str)

@app.route('/function/getQuotes', methods=['POST', 'GET'])
def getQuotes_route():
        print("request @getQuotes arrived...")
        content = request.get_json()
        response = {}
        if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getQuoteHistory')):
            response = Main.getQuoteHistory(content)
        if ('error' in content):
            response['error'] = content['error']
            return json.dumps(response, default=str)
        return json.dumps(response, default=str)

@app.route('/function/getCurrentEvent', methods=['POST', 'GET'])
def getCurrentEvent_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getCurrentEvent'

@app.route('/function/getRequestList', methods=['POST', 'GET'])
def getRequestList_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getRequestList'

@app.route('/function/getTrends', methods=['POST', 'GET'])
def getTrends_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getTrends'

@app.route('/function/getAllUsers', methods=['POST', 'GET'])
def getAllUsers_route():
    print("request @getAllUsers arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getAllUsers')):
        response = Main.getAllUsers(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)

@app.route('/function/getUsersOfType', methods=['POST', 'GET'])
def getUsersOfType_route():
    print("request @getUsersOfType arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getUsersOfType')):
        response = Main.getUsersOfType(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)

@app.route('/function/getProfitMargin', methods=['POST', 'GET'])
def getProfitMargin_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getProfitMargin'

@app.route('/function/setProfitMargin', methods=['POST', 'GET'])
def setProfitMargin_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to setProfitMargin'
