from bankAcc import bankAcc

class SavingAcc(bankAcc):


    def __init__(self,initialAmt, AccNo):
        super().__init__(initialAmt, AccNo)
        print("Congratulations!! your Savings Bank Account " + str(self._AccNo) +
              " is created with initial amount: " + str(self._amount))
       # print("Congratulations! Your Savings account is created with account number "+ str(self._AccNo))

    def SavingDep(self, amount):
        d = amount *  3 / 100
        Total_amount = amount + d
        print(str(d)+" interest is added to your deposit in account")
        self.depCash(Total_amount)
