def addVat(prize, vatRate):
    return prize * (100 + vatRate)/100

orders = [100, 150, 200]

for price in orders:
    finalAmount = addVat(price, 10)
    print(f"Original: {price}, Final with VAT: {finalAmount}")