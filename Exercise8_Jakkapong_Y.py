print("----------- xyc Shop -----------")
username = input("username : ")
password = input("password : ")
if username == "xyc123" and password == "pass123" :
    i7 = 5200
    gtx1660ti = 9200
    ssd = 2500
    print("---- wellcome to xyc Shop ----")
    print("choose the product")
    print(" 1.) i7-10750H  - 5200 THB ")
    print(" 2.) GTX1660ti  - 9200 THB ")
    print(" 3.) SSD 520 GB - 2500 THB ")
    product = input("Put number what product you want : ")
    if product == "1" :
        ni7 = int(input("How many i7-10750H do you want? : "))
        total1 = i7 * ni7
        print("Total :", total1, "THB")
        print("------- Thank you <3 -------")
    elif product == "2" :
        nGTX = int(input("How many GTX1660ti do you want? : "))
        total2 = gtx1660ti * nGTX
        print("Total :", total2, "THB")
        print("------- Thank you <3 -------")
    elif product == "3":
        nSSD = int(input("How many SSD 520 GB do you want? : "))
        total3 = ssd * nSSD
        print("Total :", total3, "THB")
        print("------- Thank you <3 -------")






