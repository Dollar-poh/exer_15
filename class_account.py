
class Account:
    numCreated = 0

    def __init__(self, initial_balance, name, ni_number, address):
        self._balance = initial_balance
        self._name = name
        self._account_number = ni_number[2:]
        self.__address = address
        Account.numCreated += 1


    def deposit(self, amount):
        self._balance += amount
        return

    def withdraw(self, amount):
        self._balance -= amount
        return

    # apply overdraft charges if below zero
    def makecharges(self):
        while self._balance < 0:
            self._balance -= 20
            print(self._name, "you are overdrawn and have been charged £20")
            break

    def getbalance(self):
        return self._balance


# create child class of Account and add attribute of interest rate and monthly interest method
class Saver(Account):
    numCreated = 0
    def __init__(self, initial_balance, name, ni_number, address):
        super().__init__(initial_balance, name, ni_number, address)
        self.interest_rate = 0.36
        self._balance = initial_balance
        self.__address = address
        Saver.numCreated += 1
        self._account_number = ni_number[1:] + " Monthly Saver"


    def add_monthly_interest(self): # new method in child class
        if issubclass(Saver, Account):  # this is to check sub class has been created
            print("--Saver is a subclass of Account--")
        self._interest = self.interest_rate * self._balance
        print(self._interest, "interest earned this month")
        self._balance += self._interest
        return self._balance


# create child class of Saver
class Annualsaver(Saver):
    numCreated = 0
    def __init__(self, initial_balance, name, ni_number, address):
        super().__init__(initial_balance, name, ni_number, address)
        self._balance = initial_balance
        self._interest_rate = 5.8
        Annualsaver.numCreated += 1

    # override method from Saver() as only yearly interest to be paid
    def add_monthly_interest(self):
        print("Monthly interest is not applied to this account")


    def add_annual_interest(self):  # new method nb would check opening date before adding annual interest with account_open_date
            self._balance = self.interest_rate * self._balance
            return self._balance

