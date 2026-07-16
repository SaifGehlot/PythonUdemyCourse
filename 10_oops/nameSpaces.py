class Chai:
    origin= "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# Creating objects from class chai

masala = Chai()
print(f"Masala {Chai.origin}")
print(f"Masala {Chai.is_hot}")

masala.is_hot = False

print("Class: ", Chai.is_hot)
print("Masala ", Chai.is_hot)
masala.flavour = "Mint"
print(masala.flavour)
