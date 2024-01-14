class BankCustomer:
    def __init__(self, name, customer_ID,accounts=[]): #accounts supposed to be a list
        self.__name = name
        self.__customer_ID = customer_ID
        self.__accounts = accounts

    # get function
    def get_name(self):
        return self.__name

    def get_customer_ID(self):
        return self.__customer_ID

    def get_accounts(self):
        return self.__accounts
    
    # set functions
    def set_name(self,new):
        self.__name=new

    def set_customer_ID(self,new):
        self.__customer_ID=new

    def set_accounts(self,new):
        self.__accounts=new
   # Methods
    def display_c(self):
        print(f"Customer Name: {self.get_name()}, Customer ID: {self.get_customer_ID()}")


    def open_c(self, account):
        self.__accounts.append(account)

    def close_c(self, account):
        self.__accounts.remove(account)


   #String

    def __str__(self):
        items = ""
        for item in self.__accounts:
            items += item.__str__() + "\n"

        return f"Name: {self.get_name():<20} Customer ID: {self.get_customerID:<20}\n\n Accounts :\n{items}"
  


