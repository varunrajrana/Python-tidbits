class Account:
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def __str__(self):
        return ('Account owner: '+ str(self.owner))+"\n" +('Account balance:'+str(self.balance))

    def deposit(self,amtadded):
        self.balance+=amtadded
        print("Deposit Accepted. New balance: "+str(self.balance))

    def withdraw(self,amtwith):
        if (self.balance>=amtwith):
            self.balance-=amtwith
            print("Withdrawl Accepted. New balance: "+str(self.balance))
        else:
            print("Funds Unavailable! Current balance: "+str(self.balance))

acct1=Account('Varun',100)

print(acct1)

acct1.deposit(100)

acct1.withdraw(400)