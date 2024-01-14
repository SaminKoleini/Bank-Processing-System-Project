from CheckingAccount import CheckingAccount

class PersonalCheckingAccount(CheckingAccount):
    def __init__(self, account_number, account_name, balance, maximum_overdraft, address):
        super().__init__(account_number, account_name, balance, maximum_overdraft)
        self.__address = address

    def get_address(self):
        return self.__address

    def set_address(self,new):
        self.__address=new

    def __str__(self):
        return f"{super().__str__()} \n with address: {self.get_address()}"
