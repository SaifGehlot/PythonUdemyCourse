class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cupTwo = Chaicup()
cupTwo.size = 100
print(Chaicup.describe(cupTwo))