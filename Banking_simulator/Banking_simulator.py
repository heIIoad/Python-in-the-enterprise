#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.


class Bank:
    def __init__(self, name, surname, age, city, address, funds):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.address = address
        self.funds = funds

    def depositMoney(self, money):
        self.funds += money
        print("Money has been deposited. Current funds on your account: " + str(self.funds))

    def withdrawMoney(self, money):
        self.funds -= money
        if self.funds < 0:
            print("not enough money to withdrow that much money")
            self.funds += money
        else:
            print("Money has withdrown. Current funds on your account: " + str(self.funds))
    
    def moneyTransfer(self, receiverObj, money):
        self.funds -= money
        if self.funds < 0:
            print("not enough money to transfer that much money")
            self.funds += money
        else:
            receiverObj.funds += money


oldAccount = Bank("Adrian", "Stepnik", 23, "Kraków", "Nowa Huta", 4000)
#for program to work you first have to create an account otherwise not defined variable will cause an error"
#for that to work properly I would handle those exceptions but didn't have time for that
while 1:
    print("Options:")
    print("1. Create account:")
    print("2. Deposit money")
    print("3. Withdrow money")
    print("4. Transfer money to other account")
    optionChoice = input("What option do you want to chose?: ")
    intOptionChoice = int(optionChoice)

    if intOptionChoice == 1:
        print("1. Create account:")
        name = input("Whats your name?: ")
        surname = input("Whats your surname?: ")
        age = input("Whats your age?: ")
        city = input("Whats your city?: ")
        address = input("Whats your address?: ")
        funds = 0
        newAccount = Bank(name, surname, age, city, address, funds)
    elif intOptionChoice == 2:
        money = input("how much money you want to deposit?: ")
        newAccount.depositMoney(money)
    elif intOptionChoice == 3:
        money = input("how much money you want to withdraw?: ")
        newAccount.withdrawMoney(money)
    elif intOptionChoice == 4:
        money = input("how much money you want to transfer?: ")
        newAccount.moneyTransfer(oldAccount, money)
    else:
        print("unknown option")