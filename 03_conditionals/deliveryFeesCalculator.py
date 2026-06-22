order_amount = int(input("Enter Your Order Amount: "))
delivery_fees = 0 if order_amount > 300 else 30
print(f"Your Delivery Fees: {delivery_fees}")