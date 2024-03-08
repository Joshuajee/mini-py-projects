class Account:
    
    _balance = 0
    
    def getAcctBal(x):
        return x._balance
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        self.__withdraw(amount)
        
    def tranfer(self, account, amount):
        account.deposit(amount)
        self.__withdraw(amount)
    
    def __withdraw(self, amount):
        if (amount > self._balance):
            raise Exception("Amount Greater than balance")
        self._balance -= amount
        

favor = Account()
ola = Account()

print("Favour's Bal: ", favor.getAcctBal())
print("Ola's Bal   : ", ola.getAcctBal())

favor.deposit(1000)
ola.deposit(5000)

print("Favour's Bal: ", favor.getAcctBal())
print("Ola's Bal   : ", ola.getAcctBal())

favor.withdraw(700)
ola.withdraw(2000)

print("Favour's Bal: ", favor.getAcctBal())
print("Ola's Bal   : ", ola.getAcctBal())

ola.tranfer(favor, 1000)

print("Favour's Bal: ", favor.getAcctBal())
print("Ola's Bal   : ", ola.getAcctBal())
