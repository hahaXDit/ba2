class User:        # here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account_balance += amount    # the specific user's account increases by the amount of the value received
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name,",", self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

rat = User("rat","rat.gmail.com")
#jane = User("Jane", "jane@jane.com")
rat.make_deposit(50).make_deposit(50)
# jane.make_deposit(50)
#rat.transfer_money(jane, 50)
rat.display_user_balance()