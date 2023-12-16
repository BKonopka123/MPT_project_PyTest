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
        if ("admin" in self.account.username  or any(self.account.username == s for s in registers.get_emails())) and self.account.password == 'admin':
            self.logins.logged()
            return True
        else:
            return False


class Registers:
    def __init__(self):
        self.count = 0
        self.emails = []


    def registered(self, register):
        self.count += 1
        self.emails.append(register.email)


    def get_emails(self):
        return self.emails


registers = Registers()


class Register:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def register(self):
        if any(self.email == s for s in registers.get_emails()):
            return False
        if '@' not in self.email:
            return False
        registers.registered(self)
        return True
