chaiType = "Plain"

def frontDesk():
    def kitchen():
        global chaiType
        chaiType = "Irani"
    kitchen()

frontDesk()
print("Chai Type", chaiType)