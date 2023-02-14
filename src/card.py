import random
color = [" ♠ ", "♣", " ♥", "♦"]

value = [7, 8, 9, 10, "K", "Q", "J", "A"]

game_one = (value * 4)
game_two = (color * 7)
random.shuffle(game_one)
random.shuffle(game_two)
game = zip(game_one, game_two)

print(tuple(game))
