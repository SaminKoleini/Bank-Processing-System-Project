from CheckingAccount import CheckingAccount

class BusinessCheckingAccount(CheckingAccount):
    def __init__(self, account_number, account_name, balance, maximum_overdraft, taxID):
        super().__init__(account_number, account_name, balance, maximum_overdraft)
        self.__taxID = taxID

    def get_taxID(self):
        return self.__taxID

    def set_taxID(self,new):
        self.__taxID=new

    def __str__(self):
        return f"{super().__str__()} taxID: {self.get_taxID()}"
