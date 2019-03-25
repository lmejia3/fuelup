"""singleton"""
class Tracker:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Tracker.__instance == None:
            Tracker()
        return Tracker.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if Tracker.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Tracker.__instance = self

    __bank = {}
    def addUser(self, user):
        self.__bank[user['key']] = {'username': user['username'], 'type': user['type']}
        print(user['username'] + ' is added to the active user pool')

    def userIsActive(self, key):
        if(key in self.__bank):
            return True
        else:
            return False

    def getActiveUserInfo(self, key):
        return self.__bank['key']

    def removeUser(self, user):
        del self.__bank[user['username']]
