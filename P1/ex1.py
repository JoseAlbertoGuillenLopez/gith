class Bank:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

        
    def withdraw(self,amount):
        self.amount=amount
        self.balance=self.balance-self.amount
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
    def display(self):
        print(f"Hola soy {self.name} y tengo este dinero {self.balance}")
    

p1=Bank("juan",0)
p2=Bank("john",0)

p1.set_details()
p2.set_details()

p1.deposit(100)
p2.deposit(200)

p1.set_details()
p2.set_details()

p1.withdraw(50)
p2.withdraw(70)


p1.set_details()
p2.set_details()

