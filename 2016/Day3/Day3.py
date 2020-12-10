with open("d3_data") as f:
    puzzle = f.read().split("\n")

puzzle = [list(map(int, line.split())) for line in puzzle]

count = 0
for triangle in puzzle:
    if 2 * max(triangle) < sum(triangle):
        count += 1

print("Part 1| Number of possible triangles:", count)

count_vertical = 0
for j in range(0, len(puzzle), 3):
    for i in range(len(puzzle[0])):
        if 2 * max(puzzle[j][i], puzzle[j+1][i], puzzle[j+2][i]) < puzzle[j][i] + puzzle[j+1][i] + puzzle[j+2][i]:
            count_vertical += 1

print("Part 2| Number of vertically possible triangles:", count_vertical)
