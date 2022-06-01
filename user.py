class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = None
        self.admin = False
        self.logged = False
        self.messages = []
    
    def login(self, name, password):
        if name == self.name and password == self.password:
            self.logged = True
        else:
            message = "There was some problems with logging. Check your password or name"
            return message

    def logout(self, name):
        self.logged = False
        pass

    def send_mail(self):
        pass

    def check_mail(self):
        pass

    def edit_user(self):
        pass
