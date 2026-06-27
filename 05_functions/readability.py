def calculateBill(chai, prize_per_cup):
    return chai * prize_per_cup

myBill = calculateBill(2, 34)
print(myBill)

print(f"Order for SaifGehlot: {calculateBill(2,54)}")