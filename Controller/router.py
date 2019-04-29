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
    print("request @processOrder arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'processOrder')):
        response = Main.processOrder(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response, default=str)
    return json.dumps(response, default=str)

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

@app.route('/function/getAllTransactionHistory', methods=['POST', 'GET'])
def getAllTransactionHistory_route():
    print("request @getAllTransactionHistory arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getAllTransactionHistory')):
        response = Main.getAllTransactionHistory(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response, default=str)
    return json.dumps(response, default=str)

@app.route('/function/Pay', methods=['POST', 'GET'])
def Pay_route():
    print("request @Pay arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'Pay')):
        response = Main.Pay(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response, default=str)
    return json.dumps(response, default=str)

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

@app.route('/function/getRequestList', methods=['POST', 'GET'])
def getRequestList_route():
    print("request @getRequestList arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getRequestList')):
        response = Main.getRequestList(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response, default=str)
    return json.dumps(response, default=str)

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

@app.route('/function/getRate', methods=['POST', 'GET'])
def getRate_route():
    print("request @getRate arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'getRate')):
        response = Main.getRate(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)

@app.route('/function/setRate', methods=['POST', 'GET'])
def SetRate_route():
    print("request @getRate arrived...")
    content = request.get_json()
    response = {}
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'setRate')):
        response = Main.setRate(content)
    if ('error' in content):
        response['error'] = content['error']
        return json.dumps(response)
    return json.dumps(response)
