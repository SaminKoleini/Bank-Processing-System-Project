class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance = balance

    def display(self):
        print("Account Number:", self.__account_number)
        print("Account Name:", self.__account_name)
        print("Balance:", self.__balance)

    def get_account_number(self):
        return self.__account_number
    
    def set_account_number(self,new):
        self.__account_number=new

    def get_account_name(self):
        return self.__account_name
    def set_account_name(self,new):
        self.__account_name=new
    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def display(self):
        return f'''The account {self.get_account_number()} belongs to {self.get_account_name()} with balance {self.get_balance()}'''
        

    
