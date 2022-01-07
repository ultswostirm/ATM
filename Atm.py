class Atm(object):
    def __init__(self,Number,Pin,Amount,Balance):
        self.Number=Number
        self.Pin=Pin
        self.Amount=Amount
        self.Balance=Balance
    def CashWithdrwal(self):
        print("You have withdrawn 2000 Rupees")
    def BalanceEnquiry(self):
        print("You have 10000 Rupees in your account")
    def AddBalance(self):
        print("600 Rupees have been added to your account")
HDFC=Atm("089 567 456","SWOSTI","Rs.2000","10000")
print(HDFC.Number)
print(HDFC.Pin)
print(HDFC.Amount)
HDFC.CashWithdrwal()
print(HDFC.Balance)
HDFC.BalanceEnquiry()
HDFC.AddBalance()

