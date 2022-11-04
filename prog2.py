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
        code = int(input("Please insert PRODUCT CODE value (0-9999): "))
    except ValueError:
        print("\n\u001b[31mPRODUCT CODE must be an integer from 0-9999\u001b[0m\n")
        continue
    while not code >= 0 or not code <= 9999:
        print("\n\u001b[31mPRODUCT CODE must be an integer from 0-9999\u001b[0m\n")
        code = int(input("Please insert PRODUCT CODE value (0-9999): "))
    else:
        break
# INPUT VALIDATION FOR Product name (checks if the input contains numbers)
while True:
    name = str(input("Please insert PRODUCT NAME: "))
    res = any(chr.isdigit() for chr in str(name))
    while res == True: 
        print("\n\u001b[31mPRODUCT NAME must be a string without any numbers\u001b[0m\n")
        name = str(input("Please insert PRODUCT NAME: "))
        res = any(chr.isdigit() for chr in str(name))
    else:
        break
# INPUT VALIDATION FOR Product sale price (checks if it isn't a real number greater than 0)
while True:
    try:
        price = float(input("Please insert PRODUCT PRICE value: "))
    except ValueError:
        print("\n\u001b[31mPRODUCT PRICE must be a real number greater than 0\u001b[0m\n")
        continue
    while not price > 0:
        print("\n\u001b[31mPRODUCT PRICE must be a real number greater than 0\u001b[0m\n")
        price = float(input("Please insert PRODUCT PRICE value: "))
    else:
        break
price = "{:.2f}".format(price)
# INPUT VALIDATION FOR Product manufacturing cost (checks if it isn't a real number greater than 0)
while True:
    try:
        manucost = float(input("Please insert PRODUCT MANUFACTURING COST value: "))
    except ValueError:
        print("\n\u001b[31mPRODUCT MANUFACTURING COST must be a real number greater than 0\u001b[0m\n")
        continue
    while not manucost > 0:
        print("\n\u001b[31mPRODUCT MANUFACTURING COST must be a real number greater than 0\u001b[0m\n")
        manucost = float(input("Please insert PRODUCT MANUFACTURING COST value: "))
    else:
        break
manucost = "{:.2f}".format(manucost)
# INPUT VALIDATION FOR Stock Level (checks if it isn't an integer greater than 0)
while True:
    try:
        stock = int(input("Please insert PRODUCT STOCK LEVEL value: "))
    except ValueError:
        print("\n\u001b[31mPRODUCT STOCK LEVEL must be an integer greater than 0\u001b[0m\n")
        continue
    while not stock > 0:
        print("\n\u001b[31mPRODUCT STOCK LEVEL must be an integer greater than 0\u001b[0m\n")
        stock = int(input("Please insert PRODUCT STOCK LEVEL value: "))
    else:
        break
# INPUT VALIDATION FOR  Estimated Monthly Units Manufactured (checks if it isn't an integer greater than or equal to 0)
while True:
    try:
        monthlymanu = int(input("Please insert ESTIMATED MONTHLY UNITS MANUFACTURED value: "))
    except ValueError:
        print("\n\u001b[31mESTIMATED MONTHLY UNITS MANUFACTURED must be an integer greater than or equal to 0\u001b[0m\n")
        continue
    while not monthlymanu >= 0:
        print("\n\u001b[31mESTIMATED MONTHLY UNITS MANUFACTURED must be an integer greater than or equal to 0\u001b[0m\n")
        monthlymanu = int(input("Please insert ESTIMATED MONTHLY UNITS MANUFACTURED value: "))
    else:
        break
# PRINTS ALL INPUTS FOR USER TO SEE
print("\nProduct code: " + str(code)) 
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
for i in range(1,13):
    product.stock += product.monthlymanu
    deviation = random.randint(-10,10)
    monthlysold = product.monthlymanu + deviation
    # CHECK FOR NEGATIVE STOCK -> deviation DECREASES BY ONE UNTIL IT DOESN'T GO BELOW 0 ANYMORE     
    while (product.stock - monthlysold) < 0:
        deviation -= 1
        monthlysold = product.monthlymanu + deviation
        # CHECKS FOR NEGATIVE MONTHLY SOLD -> monthlysold INCREASES BY 1 UNTIL IT IS NO LONGER NEGATIVE
        while monthlysold < 0:
            monthlysold+=1
        missedsales += 1
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
