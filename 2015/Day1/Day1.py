with open("d1_data") as f:
    puzzle = f.read()

opens = 0
closed = 0

for symbol in puzzle:
    if symbol == "(":
        opens += 1
    else:
        closed += 1

print("Part 1| Floor number:", opens - closed)

opens = 0
closed = 0

count = 1
for symbol in puzzle:
    if symbol == "(":
        opens += 1
    else:
        closed += 1

    if opens - closed < 0:
        print("Part 2| Position of the character:", count)
        break

    count += 1

