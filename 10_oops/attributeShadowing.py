class Chai:
    temperature = "hot"
    strenghtL = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "Small"
print("After Changing", cutting.temperature)
print("Cup", cutting.cup)
print("Direct look into the class", Chai.temperature)

del cutting.temperature
# del cutting.cup
print(cutting.temperature)
# print(cutting.cup)