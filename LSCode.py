import Connection

class LS:

    @staticmethod
    def isUsernameExist(username):
        is_user_exist = False
        keys = Connection.Connection.getAccount().keys()
        
        for key in keys:
            if username == key:
                is_user_exist = True
        return is_user_exist
    
    def verifyPassword(username, password):
        is_user_exist = LS.isUsernameExist(username)
        
        if (is_user_exist):
            if(Connection.Connection.getUser(username).getPassword() == password):
                return True
        
        return False
    
    @staticmethod
    def signup(username, password, confirmed_password):
        is_user_exist = LS.isUsernameExist(username)
        
        if(not is_user_exist and password == confirmed_password):
            Connection.Connection.addUser(username, password)
            Connection.Connection.saveData()
            return True
        else:
            return False