import random

class Product:
   def __init__(self, code, name, price, manucost,stock,monthlymanu):
    self.code=code
    self.name=name
    self.price=price
    self.manucost=manucost
    self.stock=stock
    self.monthlymanu=monthlymanu

def sure():
    global sure
    sure = input("\nAre you sure? (yes/no)\n\n").lower()
    while sure != 'yes' and sure != 'no':
        print("\nInvalid input, try again...")
        sure = input("Are you sure? (yes/no)\n").lower()
    print("\nVery well.\n")

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
    name = str(input("Please insert PRODUCT NAME (string): "))
    res = any(chr.isdigit() for chr in str(name))
    while res == True: 
        print("\n\u001b[31mPRODUCT NAME must be a string\u001b[0m\n")
        name = str(input("Please insert PRODUCT NAME (string): "))
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
        price = float(input("Please insert PRODUCT PRICE value: "))
    except ValueError:
        print("\n\u001b[31mPRODUCT PRICE must be a real number greater than 0\u001b[0m\n")
        continue
    while not price > 0:
        print("\n\u001b[31mPRODUCT PRICE must be a real number greater than 0\u001b[0m\n")
        price = float(input("Please insert PRODUCT PRICE value: "))
    else:
        break

print("\n" + str(code)) 
print("\n" + str(name))
print("\n" + str(price))
print("\n" + str(manucost))










'''



manucost = input("Please insert")


stock = input("Please insert")


monthlymanu = input("Please insert")



product=Product(code,name,price,manucost,stock,monthlymanu)
'''