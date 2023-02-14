import random
colors = ["Spade ", "Clover", "Square", "Heart"]

card = [7, 8, 9, 10, "K", "Q", "J", "A"]

cards = (card * 4)
random.shuffle(cards)
print(cards)
