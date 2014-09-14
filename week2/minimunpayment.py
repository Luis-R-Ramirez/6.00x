__author__ = 'luis'

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterest = annualInterestRate/12
payment = 0
totalpaid = 0
remainingBalance = 0

for i in range(1,13):
    payment = monthlyPaymentRate*balance
    remainingBalance = balance - payment
    balance = remainingBalance + remainingBalance*monthlyInterest
    totalpaid = totalpaid + payment
    print("Month: ",i,)
    print("Minimum monthly payment: ", "%.2f"%payment)
    print ("Remaining balance: ","%.2f"%balance,)
print("Total paid: ","%.2f"%totalpaid)
print ("Remaining balance ","%.2f"%balance)





