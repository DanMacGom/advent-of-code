with open("d7_data") as f:
    puzzle = f.read().split("\n")

assignments = {}
wire_operations = {}

for element in puzzle:
    operands, results = element.split("->")
    results = results.strip()

    current_operands = operands.strip().split(" ")

    # Assignment
    if len(current_operands) == 1:
        try:
            assignments[results] = int(current_operands[0])
        except ValueError:
            pass
    else:
        if current_operands[0] == "NOT":
            wire_operations[results] = [current_operands[1], "^0xffff"]
        elif current_operands[1] == "RSHIFT":
            wire_operations[results] = [current_operands[0], ">>",  current_operands[2]]
        elif current_operands[1] == "LSHIFT":
            wire_operations[results] = [current_operands[0], "<<", current_operands[2]]
        elif current_operands[1] == "AND":
            wire_operations[results] = [current_operands[0], "&", current_operands[2]]
        elif current_operands[1] == "OR":
            wire_operations[results] = [current_operands[0], "|", current_operands[2]]

while len(assignments) < 45:
    for var in wire_operations:
        try:
            assignments[var] = eval("".join(wire_operations[var]), {"__builtins__": None}, assignments)
        except SyntaxError:
            pass
        except NameError:
            pass
        except TypeError:
            pass

for ele in assignments:
    if ele != "c" and ele != "b":
        print(wire_operations[ele])

# print(wire_operations)
# print(assignments)
# print(wire_operations)
# print(len(wire_operations))
