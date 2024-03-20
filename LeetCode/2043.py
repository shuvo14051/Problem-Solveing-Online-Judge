from typing import List 

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1-1 <= len(self.balance) and account2-1 <= len(self.balance):
            if self.balance[account1-1] >= money:
                self.balance[account2-1] += money
                self.balance[account1-1] -= money
                return True
            return False
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account-1 <= len(self.balance):
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account-1 <= len(self.balance):
            if self.balance[account-1] >= money:
                self.balance[account-1] -= money
                return True
            return False 
        return False
        
bank = Bank([10, 100, 20, 50, 30])
print(bank.balance)
bank.withdraw(3, 10)
print(bank.balance)
bank.transfer(5, 1, 20)
print(bank.balance)
bank.deposit(5, 20)
print(bank.balance)
print(bank.transfer(3, 4, 15))
print(bank.balance)
print(bank.withdraw(10, 50))
print(bank.balance)
