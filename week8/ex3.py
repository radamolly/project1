class User:
    __name = ""
    __email = ""

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def set_name(self, name):
        self.__name = name
    
    def set_email(self, email):
        self.__email = email

user = User()
user.set_name("Rada")
user.set_email("rada@gmail.com")

print(user.get_name())
print(user.get_email())