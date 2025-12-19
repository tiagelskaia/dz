

class BankAccount:
    def __init__(self):
        pass
    def deposit(self, amount):
        self.balance +=amount

    def withdraw(self, amount):
        self.balance -=amount
        if self.balance <0:
            amount = abs(self.balance)
            self.balance = 0

