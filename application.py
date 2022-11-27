import random
import logic
#   CHECK TO SEE IF USER IS SURE OF THEIR INPUTS AT THE END (breaks loop if end-user is okay with their product)
while True:
    # INPUT VALIDATION FOR Product code (breaks loop if its an integer from 0-9999)
    code=-1
    while True:
        try:
            code = int(input("Please insert PRODUCT CODE value (0-9999): "))
        except: pass
        if code >= 0 and code < 10000:
            break
        else: print("\n\u001b[31mPRODUCT CODE must be an integer from 0-9999\u001b[0m\n")
    # INPUT VALIDATION FOR Product name (breaks loop if it contains alphabetical chars and length is at least 3 chars)
    name=""
    while True:
        name = input("Please insert PRODUCT NAME: ")
        if (name.isalpha()) and len(name) > 2:
            break
        else: print("\n\u001b[31mPRODUCT NAME must contain at least three characters and have no numbers\u001b[0m\n")
    # INPUT VALIDATION FOR Product sale price (breaks loop if its a real number greater than 0)
    price=-1
    while True:
        try:
            price = float(input("Please insert PRODUCT PRICE value: "))
        except: pass
        if price > 0:
            break
        else: print("\n\u001b[31mPRODUCT PRICE must be a real number greater than 0\u001b[0m\n")
    price = "{:.2f}".format(price)
    # INPUT VALIDATION FOR Product manufacturing cost (breaks loop if its a real number greater than 0)
    manucost=-1
    while True:
        try:
            manucost = float(input("Please insert PRODUCT MANUFACTURING COST value: "))
        except: pass
        if manucost > 0:
            break
        else:
            print("\n\u001b[31mPRODUCT MANUFACTURING COST must be a real number greater than 0\u001b[0m\n")
    manucost = "{:.2f}".format(manucost)
    # INPUT VALIDATION FOR Stock Level (breaks loop if its an integer greater than 0)
    stock=-1
    while True:
        try:
            stock = int(input("Please insert PRODUCT STOCK LEVEL value: "))
        except: pass
        if stock > 0:
            break
        else: print("\n\u001b[31mPRODUCT STOCK LEVEL must be an integer greater than 0\u001b[0m\n")
    # INPUT VALIDATION FOR Estimated Monthly Units Manufactured (breaks loop if its an integer greater than or equal to 0)
    monthlymanu=-1
    while True:
        try:
            monthlymanu = int(input("Please insert ESTIMATED MONTHLY UNITS MANUFACTURED value: "))
        except: pass
        if monthlymanu >= 0:
            break
        else: print("\n\u001b[31mESTIMATED MONTHLY UNITS MANUFACTURED must be an integer greater than or equal to 0\u001b[0m\n")
    # PRINTS ALL PRODUCT INFORMATION
    print("\n~ PRODUCT INFORMATION ~\n") 
    print("Product code: " + str(code)) 
    print("Product name: " + str(name))
    print("Product price: $" + str(price))
    print("Product manufacturing cost: $" + str(manucost))
    print("Product stock level: " + str(stock))
    print("Estimated monthly units manufactured: " + str(monthlymanu))
    print("\nAre you okay with your product info? (yes/no)")
    print('If you say "no" then you may edit the product again.\n')
    sure = input("\u001b[90m> \u001b[0m").lower()
    if sure == "yes":
        print("\nVery well.")
        break
    elif sure == "no":
        print("\nVery well. You may remake your product.\n")
    else:
        break
# ASSIGNS PRODUCT INFORMATION TO OBJECT NAMED 'product' in class Product in logic
product = logic.Product(code,name,price,manucost,stock,monthlymanu)
# INITIALIZING STOCK STATEMENT RELATED VARIABLES
monthlysold=0
missedsales=0
totalsold=0
netpnl=0
missedprofit=0
# FOR LOOP SIMULATING MONTHLY PRODUCTION AND SALES
print("\n~ MONTHLY PRODUCTION AND SALES SIMULATION ~\n")
for i in range(1,13):
    product.stock += product.monthlymanu
    deviation = random.randint(-10,10)
    monthlysold = product.monthlymanu + deviation
    # CHECK FOR NEGATIVE STOCK -> monthlysold DECREASES BY ONE UNTIL IT DOESN'T GO BELOW 0 ANYMORE
    # adds 1 to missedsales for everytime it loops     
    while (product.stock - monthlysold) < 0:
        monthlysold -= 1
        missedsales += 1
    # CHECKS FOR NEGATIVE MONTHLY SOLD -> monthlysold INCREASES BY 1 UNTIL IT IS NO LONGER NEGATIVE
    # removes 1 from missedsales everytime it loops
    while monthlysold < 0:
        monthlysold += 1
        missedsales -= 1
    product.stock -= monthlysold
    totalsold += monthlysold
    print("Month " + str(i) + ":")
    print("  Units manufactured:",str(product.monthlymanu),"\n  Units sold:",str(monthlysold),"\n  Stock:",str(product.stock))
# STORES CACULATIONS FOR NET PNL INSIDE netpnl AND REFORMATS TO TWO DECIMAL POINTS 
netpnl = (float(totalsold)*float(product.price))-(float(product.monthlymanu) * float(product.manucost))
netpnl = "{:.2f}".format(netpnl)
# IF STATEMENT TO PRINT DOLLAR SIGN IN CORRECT LOCATION
# prevents dollar sign before negative sign (e.g. $-100) and formats color (green=profit, zero=white, red=loss)
if float(netpnl) > 0:
    print("\nYour Net PNL: " + "\u001b[32m$" + str(netpnl) + "\u001b[0m")
elif float(netpnl) == 0:
    print("\nYour Net PNL: $0")
else:
    str(netpnl)
    print("\nYour Net PNL: \u001b[31m" + netpnl.replace("-","-$") + "\u001b[0m")
# PRINTS DETAILS OF SALES THAT COULD NOT BE FULFILLED AND CALCULATES MISSED PROFIT FOR THE YEAR
missedprofit = float(missedsales)*float(product.price)
missedprofit = "{:.2f}".format(missedprofit)
if missedsales > 0:
    print("\nYou missed a total of",str(missedsales),"sales this year that could not be fulfilled due lack of supply!")
    print("These missed sales would have increased your profit by \u001b[32m$" + str(missedprofit) + "\u001b[0m\n")