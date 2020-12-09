with open("d1_data") as f:
    puzzle = f.read().split(", ")


class SantaSleigh:
    def __init__(self):
        self.x, self.y = 0, 0
        # Start at "up"
        self.dir_x, self.dir_y = 0, 1
        self.visited = []

    def change_direction(self, new_direction):
        # Clockwise
        if new_direction == "R":
            # up -> right
            if self.dir_x == 0 and self.dir_y == 1:
                self.dir_x, self.dir_y = 1, 0
            # right -> down
            elif self.dir_x == 1 and self.dir_y == 0:
                self.dir_x, self.dir_y = 0, -1
            # down -> left
            elif self.dir_x == 0 and self.dir_y == -1:
                self.dir_x, self.dir_y = -1, 0
            # left -> up
            else:
                self.dir_x, self.dir_y = 0, 1
        # Counter-clockwise
        else:
            # up -> left
            if self.dir_x == 0 and self.dir_y == 1:
                self.dir_x, self.dir_y = -1, 0
            # left -> down
            elif self.dir_x == -1 and self.dir_y == 0:
                self.dir_x, self.dir_y = 0, -1
            # down -> right
            elif self.dir_x == 0 and self.dir_y == -1:
                self.dir_x, self.dir_y = 1, 0
            # right -> up
            else:
                self.dir_x, self.dir_y = 0, 1

    def append_distance_position(self, distance):
        for step in range(0, distance):
            self.x += self.dir_x
            self.y += self.dir_y
            self.visited.append([self.x, self.y])

    def total_distance(self, x=None, y=None):
        if x and y:
            return abs(x) + abs(y)
        return abs(self.x) + abs(self.y)

    def visited_twice(self):
        for position in self.visited:
            if self.visited.count(position) > 1:
                print("Result part 2:", self.total_distance(position[0], position[1]))
                return


sleigh = SantaSleigh()

for direc in puzzle:
    # direc[0] is "R" or "L", direc[1:] is the distance
    sleigh.change_direction(direc[0])
    sleigh.append_distance_position(int(direc[1:]))

print("Result part 1:", sleigh.total_distance())
sleigh.visited_twice()
