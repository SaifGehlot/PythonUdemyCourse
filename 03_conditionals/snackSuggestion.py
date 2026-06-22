# availableSnacks = {"Samosa", "Cookies"}
# customerOrder = {"Samosa", "Lassi"}
# if customerOrder[availableSnacks]: 
#   print("Order done!")

snack = input("Enter Your Prefered Snack: ").lower()
print(f"User Preferred: {snack}")
if snack == 'samosa' or snack == 'cookies' :
    print(f"Great Choice!, We will serve you {snack}")
else:
    print("Sorry We Only Server Samosa and Cookies")