import os


accounts = []

def CreateAccount(name, balance, pin):
    bankAccount = BankAccount(name, balance, pin)
    accounts.append(bankAccount)

def LoadStartMenu():
   
    accountPin = None
    while accountPin == None:
        try:
            accountPin = int(input("Insert account pin: "))
        except :
            Clear()
            print("You have to enter a integer! Try again.")
       
    selectedAccount = FindAccountWithPin(accountPin)
    if selectedAccount == None:
        Clear()
        print("That is not a valid PIN")
        LoadStartMenu()

    StartTransaction(selectedAccount)

def StartTransaction(account):
   
    transactionType = None
    while transactionType == None:
        try:
            print (f"\n<============>\nAccount: {account.name}\nBalance: {account.balance}\n<============>\n")
            transactionType = int(input("<============>\n  Withdraw[1]\n  Deposit[2]\n<============>\n"))
        except:
            Clear()
            print("You have to enter an integer! Try again.")
           
    match transactionType:
        case 1:
            pass
        case 2:
            pass
        case _:
            Clear()
            print("Not a valid transaction type")
            LoadStartMenu()

    match transactionType:
        case 1:
            account.Withdraw()
        case 2:
            account.Deposit()

def Clear():
    os.system("cls")

def FindAccountWithPin(accountPin):
    for item in accounts:
        if item.pin == accountPin:
            return item
        elif item == len(accounts):
            return None


class BankAccount():
    def __init__(self, name, balance, pin) -> None:
        self.name = name
        self.balance = balance
        self.pin = pin

   

    def Withdraw(self):
        balance = self.balance
        name = self.name
        informationText = f"\n<============>\nAccount: {name}\nBalance: {balance}\n<============>\n"
        print(informationText)

        amountSet = False
        while not amountSet:
            try:
                amount = float(input("How much would you like to Withdraw? "))
            except :
                Clear()
                print("Invalid input")
                continue
            if amount <= 0:
                Clear()
                print("You can't withdraw no money!")
            elif amount > balance:
                Clear()
                print("You're too broke for that")
            else:
                amountSet = True
                continue

        self.balance -= amount
        Clear()
        print("Your account balance is now: " + str(self.balance)) #replace this with a call to a different UI function
        LoadStartMenu()

    def Deposit(self):
        balance = self.balance
        name = self.name
        informationText = f"\n<============>\nAccount: {name}\nBalance: {balance}\n<============>\n"
        print(informationText)

        amountSet = False
        while not amountSet:
            try:
                amount = float(input("How much would you like to Deposit? "))
            except :
                Clear()
                print("Invalid input")
                continue
           
            if amount <= 0:
                print("You can't deposit no money!")
            else:
                amountSet = True

        self.balance += amount
        Clear()
        print("Your account balance is now: " + str(self.balance))
        LoadStartMenu()

#(Account name, balance, pin)
CreateAccount("Gabriel Hereth", 10.6, 1234567)
CreateAccount("Jack Pit", 0.06, 321)
CreateAccount("Mista T", 100, 5317)
LoadStartMenu()