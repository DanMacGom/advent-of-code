from collections import Counter
from string import ascii_lowercase

with open("d4_data") as f:
    puzzle = f.read().split("\n")


def parse_input(room):
    checksum = room.split("[")[1][:-1]
    sector_id = room.split("[")[0][-3:]
    encrypted_name = room.split("[")[0][0:-4].replace("-", "")

    return checksum, sector_id, encrypted_name


sector_sum = 0
answer = ""
for r in puzzle:
    message = ""
    chcksm, sct_id, encname = parse_input(r)
    # Use Counter to obtain frequencies of each character. Convert to list of tuples (.most_common()) and sort
    # by value descending and then by key alphabetically. Join into a string 5 first keys and compare to checksum.
    if "".join([x[0] for x in sorted(Counter(encname).most_common(), key=lambda x: (-x[1], x[0]))[:5]]) == chcksm:
        sector_sum += int(sct_id)

        for char in encname:
            message += chr((ord(char) + int(sct_id) - 97) % 26 + 97)

        if "north" in message:
            answer = sct_id

print("Part 1| Sum of sector IDs of real rooms:", sector_sum)
print("Part 2| Sector ID of room where North Pole objects are stored:", answer)
