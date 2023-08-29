class User:
    def __init__(self, name, email):
        self.name =  name
        self.email = email
    def getuserinfo(self):
        return (self.name, self.email)
    
