import random
tokens = list(range(1, 91))

grid = [
    list(range(1, 10)),
    list(range(10, 19)),
    list(range(19, 28))
]
grid[0][8] = grid[1][8] = grid[2][8] = 0

num_grid = random.sample(tokens, k=15)
print(num_grid)