def login() :
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Login Success")
        showMenu()
    else :
        print("Try Agian")
        login()

def showMenu():
    print("Bubblegums Shop".center(30, "-"))
    print("1. Vat Calculator")
    print("2. Total Price Calculator")
    print("3. Exit")
    userSelect = str(input("Enter the Menu : "))
    return funtion(userSelect)

def funtion(userSelect) :
    while userSelect != "0":
        if userSelect == "1":
            totalPrice = int(input("Enter Price[THB] : "))
            return vatCalculate(totalPrice)
        elif userSelect == "2":
            countItem = int(input("How many Item? : "))
            return priceCaculate(countItem)
        elif userSelect == "3":
            exit()
        else:
            print("Try again")
            showMenu()
    else:
        print("Done")
        exit()

def vatCalculate(totalPrice):
    vat = 7/100
    result = totalPrice + (totalPrice*(vat))
    print("Total : ", result)
    return result, showMenu()
def priceCaculate(countItem) :
    totalPrice = 0
    for i in range(1, countItem + 1):
        x = int(input("Item No." + str(i) + " Price : "))
        totalPrice += x
    print(vatCalculate(totalPrice))

login()
