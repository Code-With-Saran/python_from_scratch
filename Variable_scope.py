#LOCAL -> ENCLOSING -> GLOBAL -> BUILT IN VARIABLE SCOPE

fashion_company="MASS"
def dress_type():
    no_of_quantity=(int(input("Enter youur uantity : ")))
    def cost():
        pay_m="gpay"
        print(f"{fashion_company} your quantity is {no_of_quantity} and your payment method is {pay_m}")
    cost()
dress_type()
print(__file__)