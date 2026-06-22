is_boiling = True
stri_count = 5
total_actions = is_boiling + stri_count
print(f"Total actions: {total_actions}") # Upcasting

milk_present = 0 # no milk
print(f"Is there milk {bool(milk_present)}")

water_hot = True
tea_added = False
can_server = water_hot or tea_added
print(f"can sever chai? {can_server}")