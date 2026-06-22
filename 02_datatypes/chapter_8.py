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