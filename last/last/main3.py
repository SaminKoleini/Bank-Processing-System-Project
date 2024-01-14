from Bank import Bank
from BankAccount import BankAccount
from SavingAccount import SavingAccount
from CheckingAccount import CheckingAccount
from PersonalSavingAccount import PersonalSavingAccount
from PersonalCheckingAccount import PersonalCheckingAccount
from BusinessCheckingAccount import BusinessCheckingAccount
from BusinessSavingAccount import BusinessSavingAccount
from BankCustomer import BankCustomer
from SortingAlgorithms import bubble_sort, selection_sort
from SearchingAlgorithms import linear_search, binary_search
from BankBranch import BankBranch

bank = Bank()

# Load bank accounts from a text file
with open('bankAccount.txt', 'r') as reader:
    for i in range(20):
        data = reader.readline().strip().split(',')

        if data[0] == "SavingAccount":
            account = SavingAccount(data[1].strip(), data[2].strip(), float(data[3]), float(data[4]))

        elif data[0] == "CheckingAccount":
            account = CheckingAccount(data[1].strip(), data[2].strip(), float(data[3]), float(data[4]))

        elif data[0] == "PersonalSavingAccount":
            account = PersonalSavingAccount(data[1].strip(), data[2].strip(), float(data[3]), float(data[4]), data[5])

        elif data[0] == "PersonalCheckingAccount":
            account = PersonalCheckingAccount(data[1].strip(), data[2].strip(), float(data[3]), float(data[4]), data[5])

        elif data[0] == "BusinessCheckingAccount":
            account = BusinessCheckingAccount(data[1].strip(), data[2].strip(), float(data[3]), float(data[4]), data[5])

        elif data[0] == "BusinessSavingAccount":
            account = BusinessSavingAccount(data[1].strip(), data[2].strip(), float(data[3]), float(data[4]), data[5])

        bank.add_a(account)


# Load bank customers from a text file
with open('bankCustomer.txt', 'r') as reader:
    for line in reader:
        data = line.strip().split(',')

        customer = BankCustomer(data[0], int(data[1]))

        for account_number in data[2:]:
            account = bank.get_account(account_number)
            customer.open_c(account)

        bank.add_c(customer)
        
while True:
    print('-'*60)
    print(' '*10+"\"Welcome to the Banking System\"")
    print('-'*60)
    print("1. Show sorted all accounts")
    print("2. show sorted all customers")
    print("3. Open a new bank account")
    print("4. Close an existing bank account")
    print("5. Deposit funds into a bank account")
    print("6. Withdraw funds from a bank account")
    print("7. Search for a bank account")
    print("8. Sort all bank accounts based on your desire option")
    print("9. Display, Add and Remove Bank Branches")
    print("10. Exit of the Banking System")

    choice = input("Enter your choice (1-10): ")
    print('-'*50)

    if choice == "1":
        print('The sorted accounts methods: 1: account_number 2: account_name 3:balance')
        s= int(input("choose 1 or 2 or 3:  "))
        if s==1:
            bank.display_sorted_a()
        elif s==2:
            bank.display_sorted_a('account_name')
        elif s==3:
            bank.display_sorted_a('balance')
    elif choice == "2":
        print('The sorted customers methods: 1: customer_ID 2: name')
        s= int(input("choose 1 or 2:  "))
        if s==1:
            bank.display_sorted_c()
        elif s==2:
            bank.display_sorted_c('name')
        else:
            print('Wrong input. Please try again.')

    elif choice == "3":
        print("To open a new Bank Account")
        print("Please select an account type:")
        print("1. Saving Account")
        print("2. Checking Account")
        print("3. Personal Saving Account")
        print("4. Personal Checking Account")
        print("5. Business Saving Account")
        print("6. Business Checking Account")
        account_type_choice = input("Enter your choice (1-6): ")

        account_number = input("Enter the account number: ")
        account_name = input("Enter the account name: ")
        balance = float(input("Enter the account balance: "))

        if account_type_choice == "1":  # Saving Account
            interest_rate = float(input("Enter the interest rate: "))
            account = SavingAccount(account_number, account_name, balance, interest_rate)

        elif account_type_choice == "2":  # Checking Account
            maximum_overdraft = float(input("Enter the maximum overdraft: "))
            account = CheckingAccount(account_number, account_name, balance, maximum_overdraft)

        elif account_type_choice == "3":  # Personal Saving Account
            account_type = input("Enter the account type: ")
            interest_rate = float(input("Enter the interest rate: "))
            account = PersonalSavingAccount(account_number, account_name, balance, interest_rate, account_type)

        elif account_type_choice == "4":  # Personal Checking Account
            maximum_overdraft = float(input("Enter the maximum overdraft: "))
            address = input("Enter the address: ")
            account = PersonalCheckingAccount(account_number, account_name, balance, address)

        elif account_type_choice == "5":  # Business Saving Account
            business_name = input("Enter the business name: ")
            interest_rate = float(input("Enter the interest rate: "))
            account = BusinessSavingAccount(account_number, account_name, balance, interest_rate, business_name)

        elif account_type_choice == "6":  # Business Checking Account
            maximum_overdraft = float(input("Enter the maximum overdraft: "))
            tax_id = input("Enter the tax ID: ")
            account = BusinessCheckingAccount(account_number, account_name, balance, maximum_overdraft, tax_id)

        else:
            print("Invalid choice. Please try again.")
            continue

        bank.add_a(account)
        print("Bank Account opened successfully!")
        print('The new account: \n', account)

    elif choice == "4":

        # Choose whether to remove an account by account number or account name
        print("Choose removing an account by 1. Account Number 2. Account Name ")
        removal_method = int(input("Enter the removal method (1 or 2): "))

        accounts = bank.get_accounts()
        if removal_method==1:
            # Display sorted accounts for the user based on account numbers to choose from
            print("Sorted Accounts based on account number:")
            bank.display_sorted_a()
            account_number = input("Enter the account number to remove: ")
        
            # Find the account with the specified account number by linear search
            account= linear_search(accounts,account_number)
            
        elif removal_method==2:
            # Display sorted accounts for the user based on account name to choose from
            print("Sorted Accounts based on account name:")
            bank.display_sorted_a('account_name')
            account_name = input("Enter the account name to remove: ")
        
            # Find the account with the specified account name by binary search
            account= binary_search(accounts, account_name)
        else:
            print('Invalid choice. Please try again.')

        print("Removing account:")
        account.display()
        bank.remove_a(account)
        print("Account removed successfully.")
        
        # Display the updated list of accounts
        if removal_method==1:
            bank.display_sorted_a()
        elif removal_method==2:
            bank.display_sorted_a('account_name')

    elif choice == "5":
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to deposit: "))
        accounts = bank.get_accounts()
        account = linear_search(accounts, account_number)
        print('Before deposite: ', account)
        if account:
            account.deposit(amount)
            print("Deposit successful.")
            print('Updated after deposite: ', account)
        else:
            print("Account not found.")
    elif choice == "6":
        account_number = input("Enter the account number: ")
        amount = float(input("Enter the amount to withdraw: "))
        accounts = bank.get_accounts()
        account=linear_search(accounts, account_number)

        if account:
            print('Before withdrawal: ', account.display())
            account.withdraw(amount)
            print('Updated after withdrawal: ', account.display())
        else:
            print("Account not found.")

    elif choice == "7":
        accounts = bank.get_accounts()
        print('Search methods: 1. account_number or 2. account_name:')
        s= int(input("Select 1 or 2: "))
        if s==1:
            account_number= input("Enter the account number: ")
            account= linear_search(accounts, account_number)
            print(account)
        elif s==2:
            account_name= input("Enter the account number: ")
            account= binary_search(accounts, account_name)
            print(account)
        else:
            print('Invalid input.')
        
    elif choice=="8":
        accounts = bank.get_accounts()
        key= int(input('''Select your desire sorting based on
1. account number 2. account name 3. balance : '''))
        sort_function= int(input('choose your prefered algorithm to sort: 1.bubble sort 2. selction sort: '))
        if sort_function==1:
             bubble_sort(accounts,key)
        elif sort_function==2:
             selection_sort(accounts, key)
        print(bank.display())

        
    elif choice == "9":
        print("1. Display all branches \n2. Add a branch \n3. Remove a branch")
        branch_choice = input("Enter your choice 1-3: ")
        if branch_choice =="1":
            print(bank.display_branches())
        elif branch_choice == "2":
            branch_name = input("Enter the branch name: ")
            branch_address = input("Enter the branch address: ")
            branch = [branch_name, branch_address]
            bank.add_branch(branch)
            
            print("Branch added successfully.")
            print("All branches: ")
            print(bank.display_branches())

        elif branch_choice == "3":
            print("Available branches:")
            branches = bank.get_branches()
            print(bank.display_branches())
            branch_index = int(input("Enter the branch index to remove: "))
            branch_index-=1
            if 0 <= branch_index < len(branches):
                branch = branches[branch_index]
                bank.remove_branch(branch)
                print("Branch removed successfully.")
            else:
                print("Invalid branch index.")

        else:
            print("Invalid choice for branch operation.")

            
    elif choice== "10":
        print("Exiting the system...")
        break
    else:
        print('Invalid choice, try again')


