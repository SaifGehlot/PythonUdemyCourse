chai_type = "Ginger"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} chai please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")

lable_text = "Chai Spécial"
enoded_lable_text = lable_text.encode("utf-8")
print(f"Non Encoded Text: {lable_text}")
print(f"Encoded Text: {enoded_lable_text}")
decoded_lable_text = enoded_lable_text.decode("utf-8")
print(f"Decoded Text: {decoded_lable_text}")
