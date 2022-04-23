class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " + self.name + " " + self.lastname + "'s cart")

customer1 = Customer()
customer1.name = "Jakkaong"
customer1.lastname = "Yamsang"
customer1.addCart()

customer2 = Customer()
customer2.name = "Pitchyut"
customer2.lastname = "Munsin"
customer2.addCart()

customer3 = Customer()
customer3.name = "Nuttapon"
customer3.lastname = "Sirisaowarut"
customer3.addCart()

customer3 = Customer()
customer3.name = "CrapCrap"
customer3.lastname = "ChaChaCha"
customer3.addCart()


