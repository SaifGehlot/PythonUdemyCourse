class Chai:
    def __init__(self, type_, strenght):
        self.type = type_
        self.strenght = strenght

# Code Duplication

class GingerChai(Chai):
    def __init__(self, type_, strenght, spiceLevel):
        self.type = type_
        self.strenght = strenght
        self.spiceLevel = spiceLevel

# Explicit Call

class GingerChai(Chai):
    def __init__(self, type_, strenght, spiceLevel):
        Chai.__init__(self, type_, strenght)
        self.spiceLevel = spiceLevel

# Super()

class GingerChai(Chai):
    def __init__(self, type_, strenght, spiceLevel):
        super().__init__(type_, strenght)
        self.spiceLevel = spiceLevel