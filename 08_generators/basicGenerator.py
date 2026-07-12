def serveChai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Mint Chai"

stall = serveChai()

for cup in stall:
    print(cup)

# Generators
def getChaiRegular():
    return ["Cup 1", "Cup 2", "Cup 3"] 

def getChaiGenerator():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chaiStall = getChaiGenerator()
print(next(chaiStall))
print(next(chaiStall))
print(next(chaiStall))

# Hands Dirty

