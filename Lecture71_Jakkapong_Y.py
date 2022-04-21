menu = []
price = []

def orderfood() :
    while True:
        menuName = input("Enter the menu.(type exit or check) :  ")
        if menuName.lower() == "exit":
            break
        elif menuName.lower() == "check" :
            return billlist()
        else :
            menuPrice = int(input("Price : "))
            menu.append(menuName)
            price.append(menuPrice)

def billlist() :
    total = 0
    print("---- My food ----")
    for i in range(len(menu)) :
        print(i+1, menu[i], price[i])
    for x in range(len(menu)) :
        total += price[x]
    print("Total :", total)

orderfood()