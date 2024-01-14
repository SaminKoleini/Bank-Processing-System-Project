from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_name, balance, maximum_overdraft):
        super().__init__(account_number, account_name, balance)
        self.__maximum_overdraft = maximum_overdraft
        

    def get_maximum_overdraft(self):
        return self.__maximum_overdraft

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.get_maximum_overdraft():
            self.set_balance(self.get_balance() - amount)
        else:
            print("Insufficient funds.")

    
    def __str__(self):
        return f'{super().display()} with overdraft limit {self.get_maximum_overdraft()}'  
