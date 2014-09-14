__author__ = 'luis'

balance = 3329
annualInterestRate = 0.2
monthlyInterest = annualInterestRate/12
payment = 0
totalpaid = 0
remainingBalance = 0
initialPay =round((balance*(1+annualInterestRate)/120))*10

payment = 0
auxbalance = balance


for i in range(1,10):
    for i in range(1,13):
        remainingBalance = balance - initialPay
        balance = remainingBalance*(1+monthlyInterest)
    print(balance)

    if balance <= 0 and balance > -120:
        payment = initialPay
        break
    elif balance > 0:
        initialPay = initialPay + 10
        balance = auxbalance
    else:
        initialPay = initialPay - 10
        balance = auxbalance
print("Lowest Payment: ",payment)









