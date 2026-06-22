# Integers

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams 
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}")

milk_liters = 14
milk_serving = 4
milk_per_serving = milk_liters / milk_serving
print(f"milk per serving {milk_per_serving}")

total_tea_bags = 13
total_tea_pots = 4
teaBags_per_pot = total_tea_bags // total_tea_pots
print(f"While tea bags per pot {teaBags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"LeftOver C pods {leftover_pods}")

base_flavour_strength = 2
scale_factor= 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"Scaled flavour strenght {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")