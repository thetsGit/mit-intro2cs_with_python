annualSalary = float(input('The starting annual salary: '))
totalCost = float(input('The cost of your dream house: '))
semiAnnualRaise = float(input('The semi-annual raise, as a decimal: '))
targetedDuration = int(input('How many months you wanna dedicate to save your down paymant, as an integer: '))
oAnnualSalary = annualSalary
portionDownPayment = totalCost  * 0.25
currentSavings = 0.0
annualReturn = 0.04
high = 1000000
low = 0
portionSaved = (high+low)/2 * 0.000001
step = 0
for month in range(1,targetedDuration+1):
        if(month%6 == 0):
            annualSalary = annualSalary + (annualSalary*semiAnnualRaise)
        monthlyReturn = currentSavings*annualReturn/12
        currentSavings = currentSavings+(annualSalary/12*1)+monthlyReturn
if (currentSavings < portionDownPayment):
    print("it is not possible to save for the down payment in 36 months")
else:
    while ( abs(portionDownPayment-currentSavings) >= 100 ):
        currentSavings = 0
        step = step + 1
        for month in range(1,37):
                if(month%6 == 0):
                    annualSalary = annualSalary + (annualSalary*semiAnnualRaise)
                monthlyReturn = currentSavings*annualReturn/12
                currentSavings = currentSavings+(annualSalary/12*portionSaved)+monthlyReturn
        if(currentSavings > portionDownPayment):
                high = portionSaved * 1000000
        else:
                low = portionSaved * 1000000
        portionSaved = (high+low)/2 * 0.000001
        annualSalary = oAnnualSalary
    print('Best savings rate:',portionSaved)
    print('Steps in bisection search:',step)
 
    

    