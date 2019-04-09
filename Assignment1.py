#This program asks for a purchase and gives the total with taxes
#Program #1
purchase = int (input('How much was the purchase?'))
countyTax = purchase * 0.02
stateTax = purchase * 0.04

total = (purchase+countyTax+stateTax)

print ('The purchase was',purchase)
print ('The state tax is',stateTax)
print ('The county tax is',countyTax)
print ('The total sale with tax is',total)



#This program asks for a restaurant bill and it calculates the tax and tip after taxes witht the total as well
#Program #2
mealCharge = int (input('What was the charge for the meal'))
tax = mealCharge * 0.0675
tip = (mealCharge + tax) * 0.15
total = (mealCharge+tax+tip)

print ('Meal charge was',mealCharge)
print ('The tax on this meal is',tax)
print ('The tip amount on this meal is',tip)
print ('The total of the bill is',total)



#This program calculates how many stocks you purchased and stock price and then calculates the total, commission, and total with commision
#Program #3
stock = int (input('How many shares of stock did you purchase?'))
stockPrice = int (input('How much was each stock?'))
stockTotal = (stock * stockPrice)
commission = (stockTotal * 0.02)
total = (stockTotal + commission)

print ('The amount paid for the stock alone is',stockTotal)
print ('The commission that must be paid to the stock-beoker is',commission)
print ('The total stock purchse plus the commission is',total)