class Account:
    
    __balance = 0
    
    def getAcctBal(x):
        return x.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        self.__withdraw(amount)
        
    def tranfer(self, account, amount):
        account.deposit(amount)
        self.__withdraw(amount)
    
    def __withdraw(self, amount):
        if (amount > self.__balance):
            raise Exception("Amount Greater than balance")
        self.__balance -= amount
        
class SavingsAccount(Account):
    
    def getBalance(self):
        return super().__balance
    
    pass

favour = SavingsAccount()

print(favour.getBalance())
