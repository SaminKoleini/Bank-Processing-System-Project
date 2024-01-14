def bubble_sort(accounts, key=1):
    n = len(accounts)
    for i in range(n-1):
        for j in range(n-i-1):
            if key == 1: # corresponding to 'account_number'
                if accounts[j].get_account_number() > accounts[j+1].get_account_number():
                    accounts[j], accounts[j+1] = accounts[j+1], accounts[j]
            elif key ==2: # corresponding to 'account_name'
                if accounts[j].get_account_name() > accounts[j+1].get_account_name():
                    accounts[j], accounts[j+1] = accounts[j+1], accounts[j]
            elif key ==3: # corresponding to 'balance'
                if accounts[j].get_balance() > accounts[j+1].get_balance():
                    accounts[j], accounts[j+1] = accounts[j+1], accounts[j]

def selection_sort(accounts, key=1):
    n = len(accounts)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if key == 1: # corresponding to 'account_number'
                if accounts[j].get_account_number() < accounts[min_index].get_account_number():
                    min_index = j
            elif key ==2: # corresponding to 'account_name'
                if accounts[j].get_account_name() < accounts[min_index].get_account_name():
                    min_index = j
            elif key ==3: # corresponding to 'balance'
                if accounts[j].get_balance() < accounts[min_index].get_balance():
                    min_index = j
        accounts[i], accounts[min_index] = accounts[min_index], accounts[i]
