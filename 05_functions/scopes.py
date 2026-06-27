def serve_chai():
    chai_type = "Masala" # Local Scope
    print(f"Inside the Function: {chai_type}")

chai_type = "Ginger"
serve_chai()
print(f"Outside the function: {chai_type}")

def chaiCounter():
    chaiOrder = "mint" #Enclosing scope

    def printOrder():
        chaiOrder = "Lemon"
        print("Inner", chaiOrder)
    print("Outer", chaiOrder)
    printOrder()

chaiOrder = "Ginger" #Global Scope
chaiCounter()
print("Global", chaiOrder)