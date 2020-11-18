# Part 1
with open("d2_data") as f:
    puzzle = f.read()

puzzle = puzzle.split()
square_feet_paper = 0
square_feet_ribbon = 0

for box in puzzle:
    dims = list(map(int, box.split("x")))
    
    combinations = [dims[0] * dims[1], dims[1] * dims[2], dims[0] * dims[2]]
    face_perimeters = [2 * dims[0] + 2 * dims[1], 2 * dims[1] + 2 * dims[2],
                       2 * dims[0] + 2 * dims[2]]
    volume = dims[0] * dims[1] * dims[2]

    square_feet_paper += 2 * sum(combinations) + min(combinations)
    square_feet_ribbon += min(face_perimeters) + volume

print("Part 1 result:", square_feet_paper)

# Part 2
print("Part 2 result:", square_feet_ribbon)
