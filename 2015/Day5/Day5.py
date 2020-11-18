import re

with open("d5_data") as f:
    puzzle = f.read().split()

# Part 1
strings_part1 = 0
strings_part2 = 0

for word in puzzle:
    if re.search(r"^(?!.*(ab|cd|pq|xy)).*$", word):
        if re.search(r"(.)\1", word) and re.search(r"(\w*[aeuio]\w*){3,}", word):
            strings_part1 += 1

    # Part 2
    if re.search():
        pass

print("Result part 1:", strings_part1)
print("Result part 2:", strings_part2)

