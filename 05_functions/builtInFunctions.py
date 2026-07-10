def chaiFlavour(flavour="Ginger"):
    """Return the flavour of the chai"""
    chaiType = "Mint"
    return flavour

print(chaiFlavour.__name__)
print(chaiFlavour.__doc__)

def generateBill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :params chai: Number of chai cups (each cup 10 Rupess)
    :params samosa: Number of samosa (each samosa 15 Rupees)
    : return: (total amount, Thank you message as strings)
    
    """

    total = chai*10 + samosa*15
    return total, "Thank you so much for visiting chaicode.com"

generateBill()