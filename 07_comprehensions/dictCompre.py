teaPricesInr = {
    "Masala Chai" : 40,
    "Green Tea" : 50,
    "Lemon Tea" : 60
}

teaPricesUsd = {tea:price / 80 for tea, price in teaPricesInr.items()}
print(teaPricesUsd)