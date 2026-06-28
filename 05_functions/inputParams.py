# chai = "ginger chai"

# def prepareChai(order):
#     print("Preparing", order)

# prepareChai(chai)
# print(chai)

# chai = [1, 2, 3]   # list are mutable

# def editChai(cup):
#     chai[0] = 42

# editChai(chai)
# print(chai)

def makeChai(tea, milk, sugar):
    print(tea, milk, sugar)

makeChai("Ginger", "Yes", "Low") # positional
makeChai(tea="Mint", sugar="2 Tsp", milk="1/2 Bowl")
 
def specialChai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

specialChai("Cinemom", "Cardomom", sweetener="Honey", foam="yes")

# def chaiOrder(order=None):
#     order.append("Masala")
#     print(order)

# chaiOrder()

def chaiOrder(order=None):
   if order is None:
       order = []
       order.append("Saif")

   print(order)

chaiOrder()