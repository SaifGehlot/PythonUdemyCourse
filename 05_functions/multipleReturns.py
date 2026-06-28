# def makeChai():
#     return "Here is your masala chai"

# returnChai = makeChai()
# print(returnChai)

def chaiWala():
    pass

print(chaiWala())

def solidCups():
    return 120

totalCups = solidCups()
print(totalCups)

def chaiStatus(cupsLeft):
    if cupsLeft == 0:
        return "Sorry, chai is over"
    return "Here's your chai sir/mam"

print(chaiStatus(0))
print(chaiStatus(5))

def chaiReport():
    return 100, 20, 10 # Solid, Remaining, Not Paid

solid, remaining, _ = chaiReport()
print("Solid", solid)
print("Remaining", remaining)