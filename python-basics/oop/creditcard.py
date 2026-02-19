class creditcard:
    def __init__(self,name,number,bank = "123Bank"):
        self.name = name
        self.number = number
        self.bank = bank
        self.balance = 0
    
    def add_amount(self,amount):
        if not(isinstance(amount,int)) or isinstance(amount,float) or (amount >= 0):
            print("add amount denied")
        else:
            self.balance += amount #add amount
        
    def withdraw_amount(self,amount):
        if not(isinstance(amount,int)) or isinstance(amount,float) or (amount >= 0):
            print("add amount denied")
        else:
            self.balance -= amount #reduce amount
        
    def __str__(self):
        info = f"Name: {self.name} \n Number: {self.number} \n Bank: {self.bank} \n Balance: {self.balance}"

        return info
    
    
    
u1 = creditcard("Robert Welker", 123456789)
print(u1)

u1.add_amount(2000)
print(u1) #displays as dictionaries

u1.withdraw_amount(500)
print(u1)
        

        