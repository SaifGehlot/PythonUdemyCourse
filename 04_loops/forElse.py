staff = [("Saif", 18), ("Mohammed", 19), ("Ayan", 17)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No one is eligible to manage the staff")