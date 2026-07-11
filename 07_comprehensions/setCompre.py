recipes = {
    "Masala Chai" : ["Ginger", "Cardmom", "Clove"],
    "Ginger chai" : ["cardmom", "milk"],
    "Spicy chai" : ["ginger", "black pepper", "clove"]
}

uniqueValues = {spice for ingredients in recipes.values() for spice in ingredients}
print(uniqueValues)

# Hands Dirty

fooballPlayer = {
    "Liverpool" : ["Salah", "Mendes", "Alex"],
    "Man U" : ["Cristiano", "Rashford", "Maguire"],
    "Man city" : ["Bernado", "Cristiano", "Alex"]
}

uniquePlayer = {player for team in fooballPlayer.values() for player in team}
print(uniquePlayer)