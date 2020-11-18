with open("d1_data") as f:
    puzzle = f.read()

opens = 0
closed = 0

for symbol in puzzle:
    if symbol == "(":
        opens += 1
    else:
        closed += 1

print("Result:", opens - closed)
