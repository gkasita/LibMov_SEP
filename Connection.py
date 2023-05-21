import ZODB, ZODB.FileStorage
import BTrees._OOBTree
import transaction

import Account

class Connection:
    storage = ZODB.FileStorage.FileStorage('libmov.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    accounts = root.get('accounts')

    if accounts is None:
        accounts = {}

    @staticmethod
    def getRoot():
        return Connection.root
    
    @staticmethod
    def getAccount():
        print('in here')
        return Connection.accounts
    
    @staticmethod
    def getUser(username):
        return Connection.accounts[username]
    
    @staticmethod
    def addUser(username, password):
        Connection.accounts[username] = Account.User(username, password)
    
    @staticmethod
    def saveData():
        Connection.root['accounts'] = Connection.accounts
        transaction.commit()

