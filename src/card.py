import random
color = [" ♠ ", "♣", " ♥", "♦"]

value = ["7", "8", "9", "10", "V", "D", "R"]

game_one = (value * 4)
game_two = (color * 7)
game = list(zip(game_one, game_two))
random.shuffle(game)

sorted(['10', '7', '8', '9', 'D', 'R', 'V'], key=lambda x: value.index(x))
game_reverse = sorted(game, reverse=True)
print(game_reverse)
# print(sorted(game, key=lambda x: x[1]))
