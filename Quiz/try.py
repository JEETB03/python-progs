class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    

user_1 = User("Jeet", "jeetkpa2003@gmail.com")
user_1.make_deposit(100)

print(user_1.name, user_1.account_balance)