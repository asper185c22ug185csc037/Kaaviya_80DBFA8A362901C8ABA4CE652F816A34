#Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
Class Bank_Account:
Def__init__(self):
    Self.balance=0
    Print(“Hello!!! Welcome to the Deposit & Withdrawal Machine”)
Def deposit(self):
    Amount=float(input(“Enter amount to be Deposited: “))
    Self.balance += amount
    Print(“\nAmount Deposited:”,amount)
Def withdraw(self):
    Amount = float(input(“Enter amount to be Withdrawn: “))
    If self.balance>=amount:
       Self.balance-=amount
       Print(“\n You Withdrew:”, amount)
Else:
       Print(“\n Insufficient balance  “)
Def display(self):
       Print(“\n Net Available Balance=”,self.balance)
# Driver code
# creating an object of class
S = Bank_Account()
# Calling functions with that classobject
s.deposit()
s.withdraw()
s.display()