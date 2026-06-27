def updateOrder():
    chaiType = "Tulsi"

    def kitchen():
        nonlocal chaiType
        chaiType = "Kesar"
    kitchen()
    
    print(f"chaiType Update: {chaiType}")

updateOrder()


