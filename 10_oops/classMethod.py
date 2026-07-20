class chaiOrder:
    def __init__(self, teaType, sweetness, size):
        self.teaType = teaType
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def fromDict(cls, orderData):
        return cls(
            orderData["teaType"],
            orderData["sweetness"],
            orderData["size"]
        )
    
    @classmethod
    def fromString(cls, orderString):
        teaType, sweetness, size = orderString.split('-')
        return cls(teaType, sweetness, size)
    
    class chaiUtils:

        @staticmethod
        def isValidSize(size):
            return size in ["Medium", "Small", "Large"]

    
order1 = chaiOrder.fromDict({"teaType": "Mint Chai", "sweetness": "High", "size": "Large"})
order2 = chaiOrder.fromString("Masala-Low-Small")

print(order1)

    

