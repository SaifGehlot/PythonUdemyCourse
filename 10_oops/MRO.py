class A:
    lable = "A: Base class"

class B(A):
    lable = "B: Masala Chai"

class C(A):
    lable = "C: Mint Chai"

class D(B, C):
    pass

cup = D()
print(cup.lable)
print(D.__mro__)