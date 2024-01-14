from BankAccount import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, account_number, account_name, balance, interest_rate):
        super().__init__(account_number, account_name, balance)
        self.__interest_rate = interest_rate

    def get_interest_rate(self):
        return self.__interest_rate

    def calculate_interest(self):
        return super().get_balance() * self.get_interest_rate()

    def __str__(self):
        return f"{super().display()} with the calculated interest: {self.calculate_interest()}"


