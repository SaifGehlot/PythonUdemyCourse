ingredients = ["water", "Milk", "Black Tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

masala_options = ["Cinnamon", "Ginger"]
chai_options = ["Milk", "Water", "Tea Leaves"]
chai_options.extend(masala_options) 
print(chai_options)
chai_options.insert(2, "Black tea")
print(chai_options)

last_added = chai_options.pop()
print(f"{last_added}")
print(f"chai: {chai_options}")
chai_options.reverse()
print(f"chai: {chai_options}")
chai_options.sort()
print(f"chai: {chai_options}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]
full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid Mix: {full_liquid_mix}")

strong_brew = ["Black tea", "Milk"] * 3
print(f"Strong tea: {strong_brew}")

raw_spice_date = bytearray(b"CINNAMON")
raw_spice_date = raw_spice_date(b"CINNA" b"CARD")
print(raw_spice_date)
