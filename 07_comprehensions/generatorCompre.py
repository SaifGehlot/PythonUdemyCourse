dailySums = [40, 1, 56, 7, 9, 12, 32]
totalCups = (sale for sale in dailySums if sale > 5)
print(totalCups)

# Hands Dirty

promoteAccToGoals = [10, 15, 5, 12, 17, 19, 4]
playerPromotion = sum(promote for promote in promoteAccToGoals if promote > 10)