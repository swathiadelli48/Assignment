account = {}
def create_account():

    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    account["name"] = name
    account["balance"] = balance

    print("Account created successfully!\n")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    print("Amount deposited!\n")

def withdraw():    
    balance = float(input("Enter initial balance: "))
    withdraw = int(input("Withdraw: "))
    balance -= withdraw
    print("Balance: ",balance)
create_account()
deposit()
withdraw()