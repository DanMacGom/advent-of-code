with open("d2_data") as f:
    puzzle = f.read().split("\n")


class Password:
    def __init__(self, pad):
        if pad == "numpad":
            self.i, self.j = 2, 2
            self.numpad = [[".", ".", ".", ".", "."],
                           [".", "1", "2", "3", "."],
                           [".", "4", "5", "6", "."],
                           [".", "7", "8", "9", "."],
                           [".", ".", ".", ".", "."]]
        elif pad == "rhombus":
            self.i, self.j = 3, 1
            self.numpad = [[".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", "1", ".", ".", "."],
                           [".", ".", "2", "3", "4", ".", "."],
                           [".", "5", "6", "7", "8", "9", "."],
                           [".", ".", "A", "B", "C", ".", "."],
                           [".", ".", ".", "D", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", "."]]

        self.password = ""

    def decrypt_numpad(self, inp):
        for command in inp:
            for ins in command:
                if ins == "U" and self.numpad[self.i - 1][self.j] != ".":
                    self.i -= 1
                elif ins == "R" and self.numpad[self.i][self.j + 1] != ".":
                    self.j += 1
                elif ins == "D" and self.numpad[self.i + 1][self.j] != ".":
                    self.i += 1
                elif ins == "L" and self.numpad[self.i][self.j - 1] != ".":
                    self.j -= 1

            self.password += self.numpad[self.i][self.j]
        return self.password


password1 = Password("numpad")
password2 = Password("rhombus")

print("Part 1| First password:", password1.decrypt_numpad(puzzle))
print("Part 2| Second password:", password2.decrypt_numpad(puzzle))
