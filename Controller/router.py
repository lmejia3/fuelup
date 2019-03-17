from flask import Flask, request
from Modules.ViewConnector import ViewConnector as vc
app = Flask(__name__)

"""
in the router module, we simply forward the coming requests to the python application.
we need to verify each request, ensuring: the user has privilege to use the requested function,
the format of the request is appropriate, and only then, call the requested function.
"""

@app.route('/')
def dosmth():
        return 'successfully received the request'

@app.route('/function/login')
def login_route():
    return 'connected to login'

@app.route('/function/registerUser')
def registerUser_route():
    return 'connected to registerUser'

@app.route('/function/modifyProfile')
def modifyProfile_route():
    return 'connected to modifyProfile'

@app.route('/function/processOrder')
def processOrder_route():
    return 'connected to processOrder'

@app.route('/function/getQuote')
def function_route():
    return 'connected to getQuote'

@app.route('/function/setUser')
def setUser_route():
    return 'connected to setUser'

@app.route('/function/unregisterUser')
def unregisterUser_route():
    return 'connected to unregisterUser'

@app.route('/function/removeUser')
def removeUser_route():
    return 'connected to removeUser'

@app.route('/function/getTransactionHistory')
def getTransactionHistory_route():
    return 'connected to getTransactionHistory'

@app.route('/function/getAllTransactionHistory')
def getAllTransactionHistory_route():
    return 'connected to getAllTransactionHistory'

@app.route('/function/getInvoices')
def getInvoices_route():
    return 'connected to getInvoices'

@app.route('/function/getCurrentEvent')
def getCurrentEvent_route():
    return 'connected to getCurrentEvent'

@app.route('/function/getRequestList')
def getRequestList_route():
    return 'connected to getRequestList'

@app.route('/function/getTrends')
def getTrends_route():
    return 'connected to getTrends'

@app.route('/function/getAllUsers')
def getAllUsers_route():
    return 'connected to getAllUsers'

@app.route('/function/getUsersOfType')
def getUsersOfType_route():
    return 'connected to getUsersOfType'

@app.route('/function/getProfitMargin')
def getProfitMargin_route():
    return 'connected to getProfitMargin'

@app.route('/function/setProfitMargin')
def setProfitMargin_route():
    return 'connected to setProfitMargin'
