class Account:
    MIN_SAVING_BALANCE = 500

    def __init__(self, account_no, account_name, account_type, balance):
        self.account_no = account_no
        self.account_name = account_name
        self.account_type = account_type.upper()
        self.balance = balance
        self._validate_type()

    def _validate_type(self):
        if self.account_type not in ("SAVING", "CURRENT"):
            raise ValueError("Invalid Account Type")

    def show(self):
        print("\nAccount Details")
        print("-----------------------")
        print("Account No   :", self.account_no)
        print("Account Name :", self.account_name)
        print("Account Type :", self.account_type)
        print("Balance      :", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if amount > self.balance:
            raise Exception("Insufficient Fund!")

        if self.account_type == "SAVING" and \
           (self.balance - amount) < self.MIN_SAVING_BALANCE:
            raise Exception("Cannot withdraw below minimum balance (500)")

        self.balance -= amount


# MAIN 
account = Account(
    input("Enter Account Number: "),
    input("Enter Customer Name: "),
    input("Enter Account Type (SAVING/CURRENT): "),
    float(input("Enter Balance: "))
)

account.show()

try:
    amount = float(input("\nEnter Amount to Withdraw: "))
    account.withdraw(amount)
    print("New Balance:", account.balance)
except Exception as e:
    print("Error:", e)
