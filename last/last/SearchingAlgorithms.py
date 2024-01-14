'''In this searching algorithm, two ways for searching is introduced.
linear_search and binary_search is put for account_number, account_name, respectively.
'''

def linear_search(accounts, account_number): #Searching the account with specified account number 
    for account in accounts:
        if account.get_account_number() == account_number:
            return account
    return None

def binary_search(accounts, account_name):   #Searching the account with specified account name 
    accounts = sorted(accounts, key=lambda x: x.get_account_name())  # Sort the accounts by account name
    low = 0
    high = len(accounts) - 1
    while low <= high:
        mid = (low + high) // 2
        account=accounts[mid]
        if account.get_account_name() == account_name:
            return account
        elif account.get_account_name() < account_name:
            low = mid + 1
        else:
            high = mid - 1
    return None
