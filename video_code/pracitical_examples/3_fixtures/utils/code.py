from typing import Any
import pytest

class Register:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    
    def register(self):
        if any((self.email == reg_email for reg_email in registered_users.get_emails()) or 
               (self.username == reg_username for reg_username in registered_users.get_usernames())):
            return False
        account = Account(self.username, self.password, self.email)
        registered_users.registered(account)
        return True
    

    def unregister(self):
        registered_users.remove_account(self)
        return True


class RegisteredUsers:
    def __init__(self):
        self.count = 0
        self.accounts = []


    def registered(self, account):
        self.count += 1
        self.accounts.append(account)


    def get_accounts(self):
        return self.accounts
    

    def get_count(self):
        return self.count
    

    def remove_account(self, account):
        self.accounts.remove(account)


    def get_emails(self):
        return [account.email for account in self.accounts]
    

    def get_usernames(self):
        return [account.username for account in self.accounts]


class Account:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def __eq__(self, other):
        return self.username == other.username and \
               self.password == other.password and \
               self.email == other.email

    
    def get_username(self):
        return self.username
    

    def get_password(self):
        return self.password
    

    def get_email(self):
        return self.email


class User:
    def __init__(self, account):
        self.account = account
        self.logged = False

    
    def login(self):
        if self.logged:
            return False
        if self.account in registered_users.get_accounts():
            self.logged = True
            return True
        else:
            return False
        
    
    def logout(self):
        if not self.logged:
            return False
        self.logged = False
        return True
    

    def do_something(self):
        return True if self.logged else False
    
    
    def is_logged(self):
        return self.logged


registered_users = RegisteredUsers()
