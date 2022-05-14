class atm(object):
    def __init__(self, cardNumber, pinNumber, amount):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.amount = amount

    def cashWithdrawal(self, amount):
        self.amount = self.amount - amount
        print("You have Withdrawn ", amount, " Rs", "Your remaining balance is ", self.amount, " Rs")


    def BalanceEnquiry(self):
        print("Your Balance is ", self.amount, " Rs")

atm1 = atm(1234, 5768, 80000)
atm1.BalanceEnquiry()
atm1.cashWithdrawal(20000)



        