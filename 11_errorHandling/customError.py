def brewChai(flavor):
    if flavor not in ["Masala", "Ginger", "Elaichi"]:
        raise ValueError("Unsupported Chai Flavour...")
    print(f"brewing {flavor} chai...")


brewChai("Masala")