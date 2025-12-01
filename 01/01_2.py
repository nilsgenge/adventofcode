
dial = 50
pw = 0

with open("input", "r") as file:
    lines = file.read().splitlines()

for line in lines:
    dir = line[0]
    num = int(line[1:])
    if dir == 'R':
        for _ in range(num):
            dial = (dial + 1) % 100
            if dial == 0:
                pw += 1
    elif dir == 'L':
        for _ in range(num):
            dial = (dial - 1 + 100) % 100
            if dial == 0:
                pw += 1

print(pw)
