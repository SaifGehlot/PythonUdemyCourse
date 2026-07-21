chaiMenu = {"Masala": 30, "Ginger": 40}

try:
    chaiMenu["Elaichi"]
except KeyError:
    print("The key that you are looking for does not exist")

print("Chai,")