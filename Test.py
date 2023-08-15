from bankAcc import bankAcc
from SavingAcc import SavingAcc
from CurrentAcc import CurrentAcc

print("_____________________Bank account B1 created_________________________________")

B1 =bankAcc(500,1001)
B1.checkBal()
B1.withCash(200)

print("_______________________Bank account B2 created____________________________________")

B2 =bankAcc(200,1002)
B2.depCash(1000)

print("______________________Transfer of money from account B2 to B1___________________")

B2.transfer(500,B1)

print("_________________Balance checking of both the accounts____________________")
B2.checkBal()
B1.checkBal()

print("___________________________Savings account_________________________________________")

S = SavingAcc(2000,1003)
S.SavingDep(500)
S.checkBal()

print("___________________________Current Account_________________________________________")

C = CurrentAcc(2000,1004)
C.depCash(500)
C.checkBal()
C.CurrentWithdraw(100)

print("______________________Transfer of money from current account to Savings account___________________")

C.transfer(500,S)

print("_________________Balance checking of both the accounts____________________")

C.checkBal()
S.checkBal()