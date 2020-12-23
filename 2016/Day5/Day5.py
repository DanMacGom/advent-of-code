import hashlib

puzzle = "wtnhxymk"
code = ""
i = 0

while len(code) < 8:
    if "00000" in hashlib.md5(bytes(puzzle + str(i), "utf-8")).hexdigest()[0:5]:
        code += hashlib.md5(bytes(puzzle + str(i), "utf-8")).hexdigest()[5]
        print(code)
    i += 1

print("Part 1| Hashing MD5 password:", code)
