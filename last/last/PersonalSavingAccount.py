from SavingAccount import SavingAccount

class PersonalSavingAccount(SavingAccount):
    def __init__(self, account_number, account_name, balance,interest_rate, account_type):
        super().__init__(account_number, account_name, balance,interest_rate)
        self.__account_type = account_type

    def get_account_type(self):
        return self.__account_type
    
    def set_account_type(self,new):
        self.__account_type=new

    def __str__(self):
        return f"{super().__str__()} \n with account type: {self.get_account_type()}"
