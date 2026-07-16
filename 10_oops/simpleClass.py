class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

gingerTea = Chai()
print(type(gingerTea) is Chai)
print(type(gingerTea) is ChaiTime)