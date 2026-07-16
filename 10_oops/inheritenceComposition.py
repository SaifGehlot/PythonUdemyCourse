class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def addSpices(self):
        print("Adding cardmom, ginger, cloves.")

class ChaiShop:
    chaiCLS = BaseChai

    def __init__(self):
        self.chai = self.chaiCLS("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chaiCLS = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chaiCLS.addSpices()