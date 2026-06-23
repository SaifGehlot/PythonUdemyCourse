names = ["Saif", "Saqlain", "Safiya", "Soleha", "Saba", "Faisal", "Junaid"]
bills = [100, 200, 250, 5, 10, 1000, 5000]

for name, idx in zip(names, bills):
    print(f"{name} Paid the amount of {idx}")