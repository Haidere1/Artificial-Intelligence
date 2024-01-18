class BankAccount:
    def __init__(self,account_number,account_holder):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
    
    def get_balance(self):
        return self.balance
    
    def display_account_info(self):
        print(""*30)
        print("Account Number : ",self.account_number )
        print("Account Holder :", self.account_holder)
        print("Available Balance : ",self.balance)
        print(""*30)


class Bank:
    def __init__(self):
        self.accounts=[]
    
    def add_account(self,account):
        self.accounts.append(account)
    
    def remove_account(self,account_number):
        acc_removed=0
        for account in self.accounts:
            if account.account_number==account_number:
                acc_removed=account
                break
        
        if acc_removed:
            self.accounts.remove(acc_removed)
            print("The account has been removed : ",account_number)
        else:
            print("ACC NOT FOUND",account_number)
    
    def find_account(self,account_number):
        for account in self.accounts:
            if account.account_number== account_number:
                return account
            
        return None
    
    def list_accounts(self):
        print("Following are all the accounts : ")
        for account in self.accounts:
            print("="*30)
            print("Account Number : " ,account.account_number)
            print("Account Owner : " ,account.account_holder)
            print("Available Balance : " ,account.balance)
            print("="*30)
            


HBL=Bank()




while True:
        print("="*30)
        print("Welcome To HBL:")
        print("1 : ADD ACCOUNT")
        print("2 : DEPOSIT")
        print("3 : WITHDRAW")
        print("4 : FIND ACCOUNT")
        print("5 : REMOVE ACCOUNT")
        print("6 : LIST ACCOUNTS")
        print("7 : EXIT")
        print("="*30)
        choice = input("Enter your choice: ")
        

        if choice == "1":
            account_number = int(input("Enter account number: "))
            account_holder = input("Enter account holder's name: ")
            account = BankAccount(account_number, account_holder)
            HBL.add_account(account)
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            account = HBL.find_account(account_number)
            if account:
                print("="*30)
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print("Deposit successful. New balance: $", account.get_balance())
                print("="*30)
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = int(input("Enter account number: "))
            account = HBL.find_account(account_number)
            if account:
                print("="*30)
                amount = float(input("Enter withdrawal amount: "))
                if account.get_balance() >= amount:
                    account.withdraw(amount)
                    print("Withdrawal successful. New balance: $", account.get_balance())
                    print("="*30)
                else:
                    print("Insufficient funds. Current balance: $", account.get_balance())
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = int(input("Enter account number: "))
            account = HBL.find_account(account_number)
            if account:
                print("="*30)
                print("Account found:")
                account.display_account_info()
                print("="*30)
            else:
                print("Account not found.")
        elif choice == "5":
            account_number = int(input("Enter account number: "))
            HBL.remove_account(account_number)
        elif choice == "6":
            HBL.list_accounts()
        elif choice == "7":
            print(""*30)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    

