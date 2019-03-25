from flask import Flask, request
from flask_cors import CORS, cross_origin
from Modules.ViewConnector import ViewConnector as vc
from Modules.Main import Main
from Modules.UserAuthenticator.Tracker import Tracker
from Modules.UserAuthenticator import UserAuthenticator as ua
import json

app = Flask(__name__)
CORS(app)

"""
in the router module, we simply forward the coming requests to the python application.
we need to verify each request, ensuring: the user has privilege to use the requested function,
the format of the request is appropriate, and only then, call the requested function.
"""

Tracker() #initializing the singleton class

user = {'username': 'username_09', 'password': 'password_09', 'key': '123'} #for testing


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
    if (vc.validateRequest(content) and ua.userIsAuthorized(content, 'modifyProfile')):
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
def function_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getQuote'

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
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getInvoices'

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
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getAllUsers'

@app.route('/function/getUsersOfType', methods=['POST', 'GET'])
def getUsersOfType_route():
    print("request @login arrived...")
    content = request.get_json()
    return 'connected to getUsersOfType'

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
