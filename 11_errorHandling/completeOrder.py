# class invalidChaiError(Exception):
#     pass

# def bill(flavor, cups):
#     menu = {"masala": 20, "ginger": 30}
#     try:
#         if flavor not in menu:
#             raise invalidChaiError("That chai is not available")
#         if not isinstance(cups, int):
#             raise TypeError("Number of cups must be an integer")