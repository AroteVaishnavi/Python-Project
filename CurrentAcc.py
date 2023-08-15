from bankAcc import bankAcc

class CurrentAcc(bankAcc):

    def __init__(self,initialAmt,AccNo):
        super().__init__(initialAmt,AccNo)
        print("Congratulations!! your Current Bank Account " + str(self._AccNo) +
              " is created with initial amount: " + str(self._amount))
        #print("Congratulations! Your Current account is created with account number "+ str(self._AccNo))


    def CurrentWithdraw(self, amount):
        amount += 200
        print("Charges of INR 200 is applicable to your withdraw from account")
        self.withCash(amount)