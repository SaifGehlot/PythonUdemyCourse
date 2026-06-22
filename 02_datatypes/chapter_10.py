chai_order = dict(type='Masala Chai', size='Large', sugar=2)
print(f"Chai Order: {chai_order}")

chai_recipe = {}
chai_recipe['base'] = "Black Tea"
chai_recipe['liquid'] = "Milk"
print(f"Recipe Base: {chai_recipe}")
del chai_recipe['liquid']
print(f"Recipe Base: {chai_recipe}")

chai_order = dict(type='Ginger Chai', size='Medium', sugar=3)

# print(f"Chai Order Keys : {chai_order.keys()}")
# print(f"Chai Order Values : {chai_order.values()}")
# print(f"Chai Order Items : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed Last Item: {last_item}")

extra_spices = {"Cinnamon": "curshed", "Ginger": "Sliced"}
chai_recipe.update(extra_spices)
print(f"Updated Chai Recipe: {chai_recipe}")

customer_note = chai_order.get('note', "No note")
print(f"Customer note is: {customer_note}")