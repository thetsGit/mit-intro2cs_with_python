annualSalary = float(input('The starting annual salary: '))
portionSaved = float(input('The portion of salary to be saved, as a decimal: '))
totalCost = float(input("The cost of your dream home: "))
portionDownPayment = totalCost  * 0.25
currentSavings = 0.0
annualReturn = 0.04
totalMonths = 0
while ( currentSavings < portionDownPayment):
    monthlyReturn = currentSavings*annualReturn/12
    currentSavings = currentSavings+(annualSalary/12*portionSaved)+monthlyReturn
    totalMonths = totalMonths + 1
print('Number of months:',totalMonths)