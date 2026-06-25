value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible, remainder is {remainder}")

value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")

available_sizes = ["small", "medium", "Large"]

if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")

flavours = ["masala", "ginger", "lemon", "mint"]
print(f"Available flavours: {flavours}")

while (flavour := input("Enter Your Tea Flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"You choose {flavour} chai")
