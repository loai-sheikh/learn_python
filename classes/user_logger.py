class userLogger:
    def __init__(self, login, password):
        self.login = login
        self.__password = password
        print(f"user {self.login} created.")

    def loginUser(self,login,password):
        if (self.login ==login and self.__password == password):
            print("user logged in")
        else:
            print("wrong password!")
    
    def changePassword(self,oldPass, newPass):
        if (self.__password == oldPass):
            self.__password = newPass

userObj = userLogger("bob","1234")
userObj.loginUser("bob","1234")
userObj.changePassword("1234","123")
userObj.loginUser("bob","123")
