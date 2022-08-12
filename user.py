class User:

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.admin = False
        self.logged = False
        self.messages = []

    def __str__(self):
        return f"{self.name} logged: {self.logged} admin: {self.admin}"
