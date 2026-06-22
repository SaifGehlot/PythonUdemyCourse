#prizesAcctoCups = {"Small": "10rs", "Medium": "15rs", "Large" : "20rs"}
#userInput = input("Enter Your Cup Size: ").lower()
#print(f"User Preferred Size: {userInput}")
#arrayKeysCond = prizesAcctoCups.keys()
#arrayValuesCond = prizesAcctoCups.values()
#if userInput:
#    print(f"Prize for your preferred Cup Size is: {arrayValuesCond}")

cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "Small" :
    print("Prize is 10")
elif cup == "Medium" :
    print("Prize is 15")
elif cup == "Large" :
    print("Prize is 20")
else :
    print("Invalid Cup Size")            