
def printState():
    print()
    for row in rows:
        print("".join(row))


with open("input", "r") as file:
    rows = [list(line) for line in file.read().splitlines()]

# simulate
for y, row in enumerate(rows):
        for x, column in enumerate(row):
            if y<len(rows)-1:
                if rows[y][x] == 'S' and rows[y+1][x] != '|':
                    rows[y+1][x] = '|'
                if rows[y][x] == '|' and rows[y+1][x] == '.':
                    rows[y+1][x] = '|'
                if rows[y][x] == '|' and rows[y+1][x] == '^':
                    rows[y+1][x-1] = '|'
                    rows[y+1][x+1] = '|'

printState()

# count
splits = 0
for y, row in enumerate(rows):
        for x, column in enumerate(row):
             if y>0:
                if rows[y][x] == '^' and rows[y-1][x] == '|':
                     splits += 1

print("Splits: " + str(splits))


