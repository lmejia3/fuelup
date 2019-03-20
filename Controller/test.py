import sys
import datetime
import router as r
from Modules.Main import Main as mn
from Modules.Pricing import Pricing as pr
from Modules.UserRegistrator import UserRegistrator as ur
from Modules.ViewConnector import ViewConnector as vc
from Modules.UserAuthenticator import UserAuthenticator as ua
from Modules.UserAuthenticator.User import User
from Modules.DatabaseConnector import DatabaseConnector as dc

methods = {'ViewConnector.validateRequest': vc.validateRequest, 'ViewConnector.parseRequestData': vc.parseRequestData, 'UserAuthenticator.userIsValid': ua.userIsValid,\
           'UserAuthenticator.getUserType': ua.getUserType, 'UserAuthenticator.userIsAuthorized': ua.userIsAuthorized, 'UserAuthenticator.generateUserKey': ua.generateUserKey,\
           'UserRegistrator.emailAvailable': ur.emailAvailable,'UserRegistrator.passwordIsValid': ur.passwordIsValid, 'UserRegistrator.registerClient': ur.registerClient,\
           'UserRegistrator.registerAgent': ur.registerAgent,'UserRegistrator.registerManager': ur.registerManager,'Pricing.getQuote': pr.getQuote, 'Pricing.getTrendFactor': pr.getTrendFactor,\
           'Pricing.getUserHistoryFactor': pr.getUserHistoryFactor, 'Pricing.getEventFactor': pr.getEventFactor, 'Pricing.getLocationCharge': pr.getLocationCharge,\
           'Main.login': mn.login, 'Main.registerUser': mn.registerUser, 'Main.modifyProfile': mn.modifyProfile, 'Main.processOrder': mn.processOrder,\
           'Main.getQuote': mn.getQuote, 'Main.setUser': mn.setUser, 'Main.unregisterUser': mn.unregisterUser, 'Main.removeUser': mn.removeUser,\
           'Main.getTransactionHistory': mn.getTransactionHistory, 'Main.getAllTransactionHistory': mn.getAllTransactionHistory, 'Main.getInvoices': mn.getInvoices,\
           'Main.getCurrentEvent': mn.getCurrentEvent, 'Main.getRequestList': mn.getRequestList, 'Main.getTrends': mn.getTrends, 'Main.getAllUsers': mn.getAllUsers,\
           'Main.getUsersOfType': mn.getUsersOfType, 'Main.getProfitMargin': mn.getProfitMargin, 'Main.setProfitMargin': mn.setProfitMargin}
validCommands = ['@','<','>','~']
details = False


def Invoke(fname, params):
    if(fname in methods):
        return methods[fname](*params)
    else:
        print('@invoke function ' + fname + ' is not registered in the test.py code. Stopping the test...')
        quit()



def getVariable(type,var):
    if(type == 'string'):
        return var[0]
    elif(type == 'int'):
        return int(var[0])
    elif(type == 'float'):
        return float(var[0])
    elif(type == 'bool'):
        if(var[0] in ['False','false','0']):
            return False
        else:
            return True
    elif(type == 'user'):
        return User(var[0],var[1],var[2],var[3],var[4])
    else:
        print('@getVariable type ' + type + ' not supported. Stopping the test...')
        quit()

def parseFile(file_name):
    with open('test/'+file_name) as f:
        fname = 'default'
        started = False
        results = []
        inputs = []
        bar = ''
        score = 0
        counter = 1;
        for line in f:
            command = line[0]

            isComment = True
            for c in validCommands:
                if(command == c):
                    isComment = False
            if(isComment):
                continue

            line = line[1:]
            if(line[len(line)-1] == '\n'):
                line = line[:-1]

            if(command == '~'):
                print(line)
            elif(command == '@'):
                if(not started):
                    started = True
                else:
                    if(details):
                        if(counter-1 != 0):
                            print('score: ' + str(int(score/(counter-1)*100)) + '%' + ' or ' + str(score) + '/' + str(counter-1))
                        else:
                            print('score: 0/0, no entries')
                    else:
                        print(str(score) + '/' + str(counter-1))
                fname = line
                counter = 1
                inputs = []
                bar = ''
                score = 0
                print('~~~~~~~~~~~~~~~~~')
                print('now testing function ' + fname)
            else:
                calls = []
                temp = line.split('(')
                type = temp[0]
                del temp[0]
                for p in temp:
                    if(p.find('),') != -1):
                        sp = p.split('),')
                        param = sp[0]
                        var = param.split('+')
                        calls.append(getVariable(type,var))
                        type = sp[1]
                    elif(p.find(')') != -1):
                        param = p[0:len(p)-1]
                        var = param.split('+')
                        calls.append(getVariable(type, var))

                if(command == '>'):
                    inputs.append(line)
                    start_time = datetime.datetime.now()
                    results.append([Invoke(fname, calls), 0])
                    results[-1][1] = (datetime.datetime.now() - start_time).microseconds
                elif(command == '<'):
                    status = 'Failed'
                    out = results.pop()
                    if(calls[0] == out[0]):
                        status = 'Passed'
                        score += 1
                    if(not details):
                        print(str(counter) + ": " + str(status))

                    else:
                        print()
                        print('***** Test Case '+str(counter)+' *****')
                        print('input: ' + inputs[counter-1])
                        print('output: ' + str(out[0]) + '   expected: ' + str(calls[0]) + '   status: ' + status + '   execution time: ' + str(out[1]) + ' microseconds')
                        print('*****')
                    counter += 1
        if(details):
            if (counter - 1 != 0):
                print('score: ' + str(int(score / (counter - 1) * 100)) + '%' + ' or ' + str(score) + '/' + str(
                    counter - 1))
            else:
                print('score: 0/0, no entries')
        else:
            print(str(score) + '/' + str(counter - 1))

default_file = 'test_testcase.txt'
details = False
if(len(sys.argv) == 2):
    default_file = sys.argv[1]
elif(len(sys.argv) == 3):
    default_file = sys.argv[1]
    if(sys.argv[2] == 'True'):
    	details = bool(sys.argv[2])
parseFile(default_file)




