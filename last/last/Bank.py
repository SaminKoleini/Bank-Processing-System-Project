class Bank:
    def __init__(self, accountsList=[], customerList=[], branchesList=[]):
        self.__accounts = accountsList
        self.__customers = customerList
        self.__branches = branchesList

    # Getter methods
    def get_accounts(self):
        return self.__accounts

    def get_customers(self):
        return self.__customers

    def get_branches(self):
        return self.__branches

    # Setter methods
    def set_accounts(self, new):
        self.__accounts = new

    def set_customers(self, new):
        self.__customers = new

    def set_branches(self, new):
        self.__branches = new

    # Methods
    def add_a(self, account):
        self.__accounts.append(account)

    def remove_a(self, account):
        self.__accounts.remove(account)

    def add_c(self, customer):
        self.__customers.append(customer)

    def remove_c(self, customer):
        self.__customers.remove(customer)
        
    def display(self): 
        for account in self.get_accounts():
            print(account.display())

    def display_sorted_a(self, key='account_number'): # a modification without using sort algorithms
        if key == 'account_number':
            sorted_accounts = sorted(self.__accounts, key=lambda x: x.get_account_number())
        elif key == 'account_name':
            sorted_accounts = sorted(self.__accounts, key=lambda x: x.get_account_name())
        elif key == 'balance':
            sorted_accounts = sorted(self.__accounts, key=lambda x: x.get_balance())

        for account in sorted_accounts:
            print(account.display())

    def display_sorted_c(self, key='customer_ID'): # a modification without using sort algorithms
        if key == 'customer_ID':
            sorted_customers = sorted(self.__customers, key=lambda x: x.get_customer_ID())
        elif key == 'name':
            sorted_customers = sorted(self.__customers, key=lambda x: x.get_name())

        for customer in sorted_customers:
            print(customer.display_c())


    def add_branch(self, branch):
        self.__branches.append(branch)

    def remove_branch(self, branch):
        self.__branches.remove(branch)

    def display_branches(self):
        for i, branch in enumerate(self.__branches):
                print(f"{i + 1}. {branch[0]} - {branch[1]}")
