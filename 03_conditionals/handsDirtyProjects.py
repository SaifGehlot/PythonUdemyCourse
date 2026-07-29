# Project 01

Kettle_Boiled = False

if Kettle_Boiled:
    print("Kettle done! time to make chai")

# Project 02

userInput = input("Kindly! Write Your Prefered Order: ").lower()
print(f"User Preferred: {userInput}")

if userInput == "samosa" or userInput == "cookies":
    print("Here's Your Prefered Order")
else: 
    print("Sorry! We Are Out Of It Right Now")

# Project 03

userPreferedCupSize = input("Enter Your Cup Size: ").lower()
print(f"User Prefered Cup Size: {userPreferedCupSize}")
smallCup = 10
mediumCup = 20
largeCup = 40

if userPreferedCupSize == "small":
    print(f"Your Prefered Cup Size Prize: {smallCup}")
elif userPreferedCupSize == "medium":
    print(f"Your Prefered Cup Size Prize: {mediumCup}")
elif userPreferedCupSize == "large":
    print(f"Your Prefered Cup Size Prize: {largeCup}")
else:
    print("Invalid Cup Size")

# Project 04

deviceActivation = False
temperature = 40

if deviceActivation and (temperature > 35):
    print("High Temperature Alert!")
else:
    print("Temperature Normal")

