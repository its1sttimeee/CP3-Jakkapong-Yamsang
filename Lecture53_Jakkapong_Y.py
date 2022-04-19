def vatCaculate(price) :
    total = price + (price * 7/10)
    return total
print(vatCaculate(int(input("Price : "))))