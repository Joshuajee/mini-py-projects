class Private:
    
    __balance = 0
    
    def setBalance(self, value):
        self.__balance = value
        
    def getBalance(self):
        return self.__balance 
   
   
private = Private()

private.setBalance(100)

print(private.getBalance())