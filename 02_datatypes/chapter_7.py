masala_spices = ("cardamom", "cloves", "cinnamon")
print(masala_spices)
(spice1, spice2, spice3) = masala_spices
print(f"Main Masala Spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ration of C: {cardamom_ratio}, for G: {ginger_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ration of C: {cardamom_ratio}, for G: {ginger_ratio}")

# Membership
print(f"Is Masala Present in Masala Spices ? : {'ginger' in masala_spices}")