import hashlib

puzzle = "bgvyzdsv"

# Part 1
for i in range(999999):
    if "00000" in hashlib.md5(bytes(puzzle + str(i), "utf-8")).hexdigest()[0:5]:
        print("Part 1 result:", i)
        break

# Part 2
for i in range(9999999):
    if "000000" in hashlib.md5(bytes(puzzle + str(i), "utf-8")).hexdigest()[0:6]:
        print("Part 2 result:", i)
        break
