while True:
    try:
        code = int(input("Please insert PRODUCT CODE value (0-9999): "))
    except : pass
    if (code < 9999 and code > 0):
        break
    else: print("\n\u001b[31mPRODUCT CODE must be an integer from 0-9999\u001b[0m\n")