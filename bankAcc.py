class bankAcc:
    _amount= None
    _AccNo = None

    print("* Welcome to ABC Bank *")

    def __init__(self, initialAmt, AccNo):
        self._amount = initialAmt
        self._AccNo = AccNo
        #print("Congratulations!! Your Bank Account " + str(self._AccNo) +"is created with initial amount: "+str(self._amount))


    def depCash(self, amount):
        self._amount += amount
        print(str(amount)+" Rupees deposited in Bank Account " + str(self._AccNo))
        #print("The total account balance is: "+str(self._amount))

    def withCash(self, amount):
        if amount <=self._amount:
            self._amount -= amount
            print(str(amount) + " Rupees withdraw from Bank Account " + str(self._AccNo))
            #print("The total account balance is: " + str(self._amount))
        else:
            print("Insufficient account balance " + str(self._AccNo))

    def checkBal(self):
        print("Current balance in the account " + str(self._AccNo) + " is: ", self._amount)

    def transfer(self,amount,account):
        if amount <= self._amount:
            #account.withCash(amount)
            #self._amount -= amount
            self.withCash(amount)
            account.depCash(amount)
            print("The amount transfered from your account is: ",amount)
        else:
            print("Insufficient amount in your account to transfer.")