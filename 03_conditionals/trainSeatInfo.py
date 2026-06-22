seat_type = input("Enter Seat Type (Sleeper/AC/general/Luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No Ac, Beds available")
    case "ac":
        print("AC - Air conditioned, comfy beds")
    case "general":
        print("General - usually cheapest option")
    case "luxury":
        print("Luxury - Premium seat with meals")
    case _:
        print("Invalid seat Type")
