MIN_SAVING_BALANCE = 500


def show_account(account_no, account_name, account_type, balance):
    print("\nAccount Details")
    print("-----------------------")
    print("Account No   :", account_no)
    print("Account Name :", account_name)
    print("Account Type :", account_type)
    print("Balance      :", balance)


def withdraw(account_type, balance, amount):
    account_type = account_type.upper()

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if amount > balance:
        raise Exception("Insufficient Fund!")

    if account_type == "SAVING" and (balance - amount) < MIN_SAVING_BALANCE:
        raise Exception("Cannot withdraw below minimum balance (500)")

    if account_type not in ("SAVING", "CURRENT"):
        raise ValueError("Invalid Account Type")

    return balance - amount


# MAIN 
account_no = input("Enter Account Number: ")
account_name = input("Enter Customer Name: ")
account_type = input("Enter Account Type (SAVING/CURRENT): ")
balance = float(input("Enter Balance: "))

show_account(account_no, account_name, account_type, balance)

amount = float(input("\nEnter Amount to Withdraw: "))

try:
    balance = withdraw(account_type, balance, amount)
    print("New Balance:", balance)
except Exception as e:
    print("Error:", e)
