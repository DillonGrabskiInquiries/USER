class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)


michael = User("michael", "michael.com")
anna = User("anna", "anna.com")
joe = User("joe", "joe.com")

michael.make_deposit(100)
michael.make_deposit(100)
michael.make_deposit(100)
michael.make_withdrawal(50)
print(michael.account_balance)

anna.make_deposit(100)
anna.make_deposit(100)
anna.make_withdrawal(50)
anna.make_withdrawal(50)
print(anna.account_balance)

joe.make_deposit(150)
joe.make_withdrawal(50)
joe.make_withdrawal(50)
joe.make_withdrawal(50)
print(joe.account_balance)