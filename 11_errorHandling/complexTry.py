def serveChai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("Sorry, The Value doest exists in our flavour list")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"Chai {flavour} is served...")
    finally:
        print("Next Customer Please")

serveChai("unknown")