import random

arr = [random.randint(0, 5000) for i in range(20)] # create an array with accounts between 0 and $5000

def Menu(): # print the main menu
    print("MAIN MENU")
    print("1: Print Accounts")
    print("2: Deposit")
    print("3: Withdrawal")
    print("4: Count Under $2000")
    print("5: Generous Donor")
    print("6: Hacker Attack")
    print("7: Exit")
    return int(input("Enter Option #"))

def ChangeBalance(amount): # function to print out the previous and new balances of an account after it is changed
    print(f"Account {accNum} Previous Balance: {arr[accNum]}")
    arr[accNum] += amount
    print(f"Account {accNum} New Balance: {arr[accNum]}")

inp = Menu()
while inp != 7: # keep displaying the menu if 7 is not entered
    match inp:
        case 1:
            print("ACCOUNT BALANCES")
            for i in range(len(arr)): # print baalnces of all the accounts
                print(f"Account {i}: ${arr[i]}")
        case 2:
            print("DEPOSIT") # deposit money
            accNum = int(input("Enter account #: "))
            depAmount = int(input("Enter amount to deposit:"))
            ChangeBalance(depAmount)
        case 3:
            print("WITHDRAWAL")
            accNum = int(input("Enter account #: "))
            withdrawalAmount = int(input("Enter amount to withdrawal:"))
            if arr[accNum] >= withdrawalAmount: # check if the withdrawal amount is over the account balnce
                ChangeBalance(-withdrawalAmount)
            else:
                print("Sorry, insufficient funds.")
        case 4:
            print("COUNT UNDER $2000")
            for i in range(len(arr)):
                if arr[i] < 2000: # print the account if its under $2000
                    print(f"Account {i}: {arr[i]}")
        case 5:
            print("GENEROUS DONOR")
            amountChanged = 0
            for i in range(len(arr)):
                if arr[i] < 2000: # check if account balnce under 2000
                    ChangeBalance(500) # add balance
                    amountChanged += 1
            print(f"Accounts that recieved donation: ({amountChanged}), {amountChanged * 500} dollars donated")
        case 6:
            print("HACKER ATTACk")
            amountStolen = 0
            for i in range(len(arr)):
                amountStolen += arr[i] * 0.05 # track how much money was stolen
                arr[i] -= arr[i] * 0.05 # take the amount stolen away from the account
            print(f"Total stolen is: ${amountStolen}")
    inp = Menu() # display the menu again
