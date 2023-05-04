import ZODB, ZODB.FileStorage
import BTrees._OOBTree
import transaction
import Account
import Main

storage = ZODB.FileStorage.FileStorage('libmov.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

accounts = root['accounts']

@staticmethod
def isUsernameExist(username):
    keys = accounts.keys()
    for key in keys:
    #username already exist
        if username == key:
            return True
    return False 
        

@staticmethod
def closeConnection():
    root['accounts'] = accounts
    transaction.commit()









        



