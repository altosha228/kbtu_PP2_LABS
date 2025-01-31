class Account():
  owner = ""
  balance = 0
  def __init__(self, owner):
    self.owner = owner

  def showBalance(self):
    print(self.balance)
  
  def deposit(self, amount):
    self.balance += amount
  
  def withdraw(self, amount):
    if(amount > self.balance):
      print("Error: you can't withdraw more money than your account have")
    else:
      self.balance -= amount
  
myAccount = Account("Altair")
myAccount.withdraw(1000)
myAccount.deposit(3000)
myAccount.showBalance()
myAccount.withdraw(4000)
myAccount.withdraw(2000)
myAccount.showBalance()
