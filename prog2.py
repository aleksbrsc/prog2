import random

class Product:
   def __init__(self, code, name, price, manucost,stock,monthlymanu):
    self.code=code
    self.name=name
    self.price=price
    self.manucost=manucost
    self.stock=stock
    self.monthlymanu=monthlymanu

# FOREVER LOOP FOR HANDLING Product code INPUT VALIDATION (checks if it isn't an int from 0-9999)
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
# FOREVER LOOP FOR HANDLING Product name INPUT VALIDATION (checks if the input contains numbers)
while True:
    name = str(input("Please insert PRODUCT NAME: "))
    res = any(chr.isdigit() for chr in str(name))
    while res == True: 
        print("\n\u001b[31mPRODUCT NAME must be a string without any numbers\u001b[0m\n")
        name = str(input("Please insert PRODUCT NAME: "))
        res = any(chr.isdigit() for chr in str(name))
    else:
        break
# FOREVER LOOP FOR HANDLING Product sale price INPUT VALIDATION (checks if it isn't a real number greater than 0)
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
# FOREVER LOOP FOR HANDLING Product manufacturing cost INPUT VALIDATION (checks if it isn't a real number greater than 0)
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
# FOREVER LOOP FOR HANDLING Stock Level INPUT VALIDATION (checks if it isn't an integer greater than 0)
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
# FOREVER LOOP FOR HANDLING Estimated Monthly Units Manufactured INPUT VALIDATION (checks if it isn't an integer greater than or equal to 0)
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

print("\nProduct code: " + str(code)) 
print("Product name: " + str(name))
print("Product price: $" + str(price))
print("Product manufacturing cost: $" + str(manucost))
print("Product stock level: " + str(stock))
print("Estimated monthly units manufactured: " + str(monthlymanu) + "\n")











'''



manucost = input("Please insert")


stock = input("Please insert")


monthlymanu = input("Please insert")



product=Product(code,name,price,manucost,stock,monthlymanu)
'''
