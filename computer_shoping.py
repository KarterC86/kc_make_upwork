import math 

msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razor_blade15_price = 3696.99
asus_n16_price = 1849.79

#round()
#round(number, decimal_digits)


print(f"""the most expensive computer is the Gigabyte Aero at{gigabyte_aero_price}
the least expensive computer is the asus n16 at {asus_n16_price}


""")

#x = msi_rtxa5000_price
#print (round(x))

x = msi_rtxa5000_price
print("the msi rtxa5000 price rounded is;")
print (math.floor(x))

y = gigabyte_aero_price
print("gigabyte Aero's price rounded is;")
print (math.floor(y))

z = razor_blade15_price
print("razor blade15 price rounded is;")
print (math.floor(z))

w = asus_n16_price 
print("asus N16 price rounded is;")
print (math.floor(w))
