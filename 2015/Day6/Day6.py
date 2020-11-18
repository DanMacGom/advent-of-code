import re

with open("d6_data") as f:
    puzzle = f.read().split("\n")

# Part 1
light_grid = [[-1 for i in range(1000)] for j in range(1000)]

for instruction in puzzle:
    x1 = int(re.findall("\d+", instruction)[0])
    y1 = int(re.findall("\d+", instruction)[1])

    x2 = int(re.findall("\d+", instruction)[2])
    y2 = int(re.findall("\d+", instruction)[3])

    if "turn on" in instruction:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                light_grid[i][j] = 1

    if "turn off" in instruction:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                light_grid[i][j] = -1

    if "toggle" in instruction:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                light_grid[i][j] *= -1

lights = 0

for j in light_grid:
    lights += sum(a for a in j if a > 0)

print("Result part 1:", lights)

# Part 2
light_grid = [[0 for i in range(1000)] for j in range(1000)]

for instruction in puzzle:
    x1 = int(re.findall("\d+", instruction)[0])
    y1 = int(re.findall("\d+", instruction)[1])

    x2 = int(re.findall("\d+", instruction)[2])
    y2 = int(re.findall("\d+", instruction)[3])

    if "turn on" in instruction:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                light_grid[i][j] += 1

    if "turn off" in instruction:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                light_grid[i][j] -= 1 if light_grid[i][j] > 0 else 0

    if "toggle" in instruction:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                light_grid[i][j] += 2

lights = 0

for j in light_grid:
    lights += sum(a for a in j)

print("Result part 2:", lights)
