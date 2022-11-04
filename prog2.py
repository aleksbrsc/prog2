import random
# CREATION OF CLASS Product
class Product:
   def __init__(self, code, name, price, manucost,stock,monthlymanu):
    self.code=code
    self.name=name
    self.price=price
    self.manucost=manucost
    self.stock=stock
    self.monthlymanu=monthlymanu
# INPUT VALIDATION FOR Product code (checks if it isn't an int from 0-9999)
while True:
    try:
        code = int(input("Please insert PRODUCT CODE value (0-9999): ") or -1)
    except : pass
    if code >= 0 and code < 10000:
        break
    else: print("\n\u001b[31mPRODUCT CODE must be an integer from 0-9999\u001b[0m\n")
# INPUT VALIDATION FOR Product name (checks if the input contains numbers)
while True:
    name = input("Please insert PRODUCT NAME: ")
    if (name.isalpha()) and len(name) > 2:
        break        
    else: print("\n\u001b[31mPRODUCT NAME must contain at least three characters and have no numbers\u001b[0m\n")
# INPUT VALIDATION FOR Product sale price (checks if it isn't a real number greater than 0)
while True:
    try:
        price = float(input("Please insert PRODUCT PRICE value: ") or -1)
    except: pass
    if price > 0:
        break
    else: print("\n\u001b[31mPRODUCT PRICE must be a real number greater than 0\u001b[0m\n")
price = "{:.2f}".format(price)
# INPUT VALIDATION FOR Product manufacturing cost (checks if it isn't a real number greater than 0)
while True:
    try:
        manucost = float(input("Please insert PRODUCT MANUFACTURING COST value: ") or -1)
    except: pass
    if manucost > 0:
        break
    else:
        print("\n\u001b[31mPRODUCT MANUFACTURING COST must be a real number greater than 0\u001b[0m\n")
manucost = "{:.2f}".format(manucost)
# INPUT VALIDATION FOR Stock Level (checks if it isn't an integer greater than 0)
while True:
    try:
        stock = int(input("Please insert PRODUCT STOCK LEVEL value: ") or -1)
    except: pass
    if stock > 0:
        break
    else: print("\n\u001b[31mPRODUCT STOCK LEVEL must be an integer greater than 0\u001b[0m\n")
# INPUT VALIDATION FOR  Estimated Monthly Units Manufactured (checks if it isn't an integer greater than or equal to 0)
while True:
    try:
        monthlymanu = int(input("Please insert ESTIMATED MONTHLY UNITS MANUFACTURED value: ") or -1)
    except: pass
    if monthlymanu >= 0:
        break
    else: print("\n\u001b[31mESTIMATED MONTHLY UNITS MANUFACTURED must be an integer greater than or equal to 0\u001b[0m\n")
# PRINTS ALL INPUTS FOR USER TO SEE
print("\n~ PRODUCT INFORMATION ~\n") 
print("Product code: " + str(code)) 
print("Product name: " + str(name))
print("Product price: $" + str(price))
print("Product manufacturing cost: $" + str(manucost))
print("Product stock level: " + str(stock))
print("Estimated monthly units manufactured: " + str(monthlymanu) + "\n")
# OBJECT NAMED 'product' CREATED
product = Product(code,name,price,manucost,stock,monthlymanu)
# INITIALIZING STOCK STATEMENT RELATED VARIABLES
monthlysold=0
missedsales=0
totalsold=0
netpnl=0
# FOR LOOP SIMULATING MONTHLY PRODUCTION AND SALES
print("~ MONTHLY PRODUCTION AND SALES SIMULATION ~\n")
for i in range(1,13):
    product.stock += product.monthlymanu
    deviation = random.randint(-10,10)
    monthlysold = product.monthlymanu + deviation
    # CHECK FOR NEGATIVE STOCK -> deviation DECREASES BY ONE UNTIL IT DOESN'T GO BELOW 0 ANYMORE
    # adds 1 to missedsales for everytime it loops     
    while (product.stock - monthlysold) < 0:
        deviation -= 1
        monthlysold = product.monthlymanu + deviation
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
# prevents dollar sign before negative sign (e.g. $-100)
if float(netpnl) >= 0:
    print("\nYour Net PNL: " + "\u001b[32m$" + str(netpnl) + "\u001b[0m")
else:
    str(netpnl)
    print("\nYour Net PNL: \u001b[31m" + netpnl.replace("-","-$") + "\u001b[0m")
#prints details of sales that could not be fulfilled
if missedsales > 0:
    print("\nYou missed a total of",str(missedsales),"sales this year that could not be fulfilled due lack of supply!\n")