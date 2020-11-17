with open("data") as f:
    puzzle = f.read()

open = 0
closed = 0

for symbol in puzzle:
    if symbol == "(":
        open += 1
    else:
        closed += 1

print(open - closed)
