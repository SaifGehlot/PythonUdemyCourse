class OutOfIngredientError(Exception):
    pass

def makeChai(milk, sugar):
    if milk == 0 or sugar == 0:
      raise OutOfIngredientError("Missing milk or sugar")