def localChai():
    yield "Masala Chai"
    yield "Ginger Chai"

def importedChai():
    yield "Maatcha"
    yield "Oolong"

def fullMenu():
    yield from localChai()
    yield from importedChai()

for chai in fullMenu():
    print(chai)

def chaiOrder():
    try:
        while True:
            order = yield "Waiting for the chai order..."
    except: 
            print("stall closed, no more chai")

stall = chaiOrder()
print(next(stall))
stall.close() #cleanups the memory