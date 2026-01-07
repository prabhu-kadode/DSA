from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,name,balance):
        self.__balance= balance
        self.name = name
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print(f"{amount} Deposited")
            return
        print("invalid amount")
    @abstractmethod
    def widraw(self):
        pass
    def getBalance(self):
        return self.__balance
    def updateBalance(self,amount):
        self.__balance=amount
class SavingAccount(Account):
    def widraw(self,amount):
        if amount > self.getBalance():
            print("Low balnace")
            return
        self.updateBalance(self.getBalance()-amount)
sa = SavingAccount("prabhu",1000)
sa.widraw(100)
sa.widraw(100)
print(sa.getBalance())
        


        
