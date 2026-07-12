teaPricesInr = {
    "Masala Chai" : 40,
    "Green Tea" : 50,
    "Lemon Tea" : 60
}

teaPricesUsd = {tea:price / 80 for tea, price in teaPricesInr.items()}
print(teaPricesUsd)

# Hands Dirty

footballPlayerCostData = {
    "Ronaldo": 1000,
    "Messi": 800,
    "Neymar": 500
}

playersCostInUsd = {player:cost / 80 for player, cost in footballPlayerCostData.items()}
print(playersCostInUsd)