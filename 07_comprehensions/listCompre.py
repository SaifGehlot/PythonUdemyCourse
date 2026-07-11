menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

# Hands Dirty

footballPlayers = [
    "Neymar Jr.",
    "Vinicius Jr.",
    "Ronaldo",
    "Messi"
]

jrPlayer = [jr for jr in footballPlayers if "Jr." in jr]
print(jrPlayer)
