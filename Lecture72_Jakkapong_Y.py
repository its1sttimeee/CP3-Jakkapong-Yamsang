menu = []

def orderfood() :
    while True:
        menuName = input("Enter the menu.(type exit or check) :  ")
        if menuName.lower() == "exit":
            break
        elif menuName.lower() == "check" :
            return billlist()
        else :
            menuPrice = int(input("Price : "))
            menu.append([menuName, menuPrice])

def billlist() :
    total = 0
    print("---- My food ----")
    for i in range(len(menu)) :
        print(i+1, ".)", menu[i][0], menu[i][1])
    for x in range(len(menu)) :
        total += menu[x][1]
    print("Total :", total)

orderfood()