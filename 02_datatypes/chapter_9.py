essential_spices = {"cardomom", "ginger", "cinemom"}
optional_spices = {"cloves", "ginger", "black paper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Essential Spices Only: {only_in_essential}")

# Membership test
print(f"Is 'cloves' present in essential spices ? : {'cloves' in essential_spices}")