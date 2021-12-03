bike1 = "yamaha"
bike1_price = 400000

bike2 = "honda"
bike2_price = 550000

name = input("enter your:")
choose =  int(input("press 1 for yamaha and 2 for honda"))
print = (f"hello {name}")

if choose ==1:
    print(f"{bike1} will cost you {bike1_price}")
elif choose ==2:
    print(f"{bike2+400000} cost you {bike2_price}")
else:
    print("press only 1 and 2")
