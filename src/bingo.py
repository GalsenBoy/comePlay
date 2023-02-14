import random

tokens = list(set(range(1, 91)))
grid = []
for i in range(3):
    grid.append(random.sample(tokens, k=5))


for j in range(3):
    grid[0].append(0)
    grid[1].append(0)
    grid[2].append(0)

random.shuffle(grid[0])
random.shuffle(grid[1])
random.shuffle(grid[2])
print(grid)
#grid[0][8] = grid[1][8] = grid[2][8] = 0

#num_grid = random.sample(tokens, k=15)
#print(num_grid)
