def chaiCustomer():
    print("Welcome! what chai would you prefer")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chaiCustomer() # refering the function or storing a function
next(stall) # start the function

stall.send("Masala Chai")