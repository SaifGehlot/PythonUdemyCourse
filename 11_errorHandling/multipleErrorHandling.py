def processOrder(item, quantity):
    try:
        price = {"Masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Item not found in our inventory.")
    except ValueError:
        print("Quantity must be in number")

processOrder("ginger", 20)
processOrder("Masala", "two")