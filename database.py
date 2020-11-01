import pymongo



class Database():
    def __init__(self):
        self.cluster = pymongo.MongoClient("mongodb+srv://Dan:1234@cluster0.y2fmq.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.cluster["test"]
        self.collection = self.db["test"]

    def isUserNameExists(self, un):
        if self.collection.find_one({"username" : un}) != None:           
            return True
        return False

    def isAccountExists(self, un, pw):
        if self.isUserNameExists(un) == True:           
            userDetails = self.collection.find({"username" : un})
            for detail in userDetails:
                matchPassword = detail["password"]
            if matchPassword == pw:
                return True
        else:
            return False
    
    def createAccount(self, un, pw):
        if self.isUserNameExists(un) == True:
            return "Username Exists"
        else:
            details = {"username" : un, "password" : pw}
            self.collection.insert_one(details)
            return "account Created"


    

