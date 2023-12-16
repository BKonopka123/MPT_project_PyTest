class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Logins:
    def __init__(self):
        self.count = 0
    

    def logged(self):
        self.count += 1


    def get_count(self):
        return self.count



class Login:
    def __init__(self, account):
        self.account = account
        self.logins = Logins()


    def login(self):
        if self.account.username == 'admin' and self.account.password == 'admin':
            self.logins.logged()
            return True
        else:
            return False
        

