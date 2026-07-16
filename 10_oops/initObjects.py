class chaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    
    def summary(self):
        return f"{self.size}ml of {self.type} chai" 
    
order = chaiOrder("Masala", 200)
print(order.summary())

orderTwo = chaiOrder("Ginger", 220)
print(orderTwo.summary())