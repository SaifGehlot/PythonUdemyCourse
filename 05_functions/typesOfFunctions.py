# Pure Function

def pureChai(cups):
    return cups * 10

# Impure Function
# Not recommended
totalChai = 0
def impureChai(cups):
    global totalChai
    totalChai += 0

def pourChai(n):
    print(n)
    if n == 0:
        return "All Cups Are Poured"
    return pourChai(n-1) 

print(pourChai(4))

chaiTypes = ["Light", "Kadak", "Ginger", "Kadak"]

filterChai = list(filter(lambda item: item == "Kadak", chaiTypes))
print(filterChai)