annualSalary = float(input('The starting annual salary: '))
portionSaved = float(input('The portion of salary to be saved, as a decimal: '))
totalCost = float(input("The cost of your dream home: "))
semiAnnualRaise = float(input('The semi-annual salary raise, as a decimal: '))
portionDownPayment = totalCost  * 0.25
currentSavings = 0.0
annualReturn = 0.04
totalMonths = 0
while ( currentSavings < portionDownPayment):
    if(totalMonths != 0 and totalMonths%6 == 0):
        annualSalary = annualSalary + (annualSalary*semiAnnualRaise)    
    monthlyReturn = currentSavings*annualReturn/12
    currentSavings = currentSavings+(annualSalary/12*portionSaved)+monthlyReturn
    totalMonths = totalMonths + 1
print('Number of months:',totalMonths)