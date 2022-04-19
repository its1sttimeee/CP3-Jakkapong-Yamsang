def vatCalculate(price) :
    total = price + (price * 7/100)
    return total

print(vatCalculate(input(int("Price : "))))

