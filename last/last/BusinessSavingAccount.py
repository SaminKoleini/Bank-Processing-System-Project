from SavingAccount import SavingAccount

class BusinessSavingAccount(SavingAccount):
    def __init__(self, account_number, account_name, balance, interest_rate, business_name):
        super().__init__(account_number, account_name, balance, interest_rate)
        self.__business_name = business_name

    def get_business_name(self):
        return self.__business_name

    def set_business_name(self,new):
        self.__business_name=new

    def __str__(self):
        return f"{super().__str__()}, Business name: {self.get_business_name()}"
