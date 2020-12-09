with open("d3_data") as f:
    puzzle = f.read()

# Part 1
actual_position = [0, 0]
history_of_positions = [[0, 0]]

for symbol in puzzle:
    if symbol == "^":
        actual_position[1] += 1
    elif symbol == ">":
        actual_position[0] += 1
    elif symbol == "v":
        actual_position[1] -= 1
    elif symbol == "<":
        actual_position[0] -= 1

    if actual_position not in history_of_positions:
        history_of_positions.append(actual_position.copy())

print("Part 1| Houses that receive at least one present from Santa:", len(history_of_positions))

# Part 2
santa_position = [0, 0]
robot_position = [0, 0]

history_of_positions = [[0, 0]]

for i, symbol in enumerate(puzzle):
    if i % 2 == 0:
        if symbol == "^":
            santa_position[1] += 1
        elif symbol == ">":
            santa_position[0] += 1
        elif symbol == "v":
            santa_position[1] -= 1
        elif symbol == "<":
            santa_position[0] -= 1

        if santa_position not in history_of_positions:
            history_of_positions.append(santa_position.copy())

    else:
        if symbol == "^":
            robot_position[1] += 1
        elif symbol == ">":
            robot_position[0] += 1
        elif symbol == "v":
            robot_position[1] -= 1
        elif symbol == "<":
            robot_position[0] -= 1

        if robot_position not in history_of_positions:
            history_of_positions.append(robot_position.copy())

print("Part 2| Houses that receive at least one present from Santa and Robo-Santa:", len(history_of_positions))
