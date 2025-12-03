
maxJoltage = 0

with open("input", "r") as file:
    banks_str = file.read().splitlines()

banks_int = [[int(c) for c in s] for s in banks_str]

for bank in banks_int:
    first_char = -1
    first_char_index = -1
    for a in range(0, len(bank) -1):
        if bank[a] > first_char:
            first_char = bank[a]
            first_char_index = a
    
    second_char = -1
    for b in range(1, len(bank)):
        if bank[b] > second_char and b > first_char_index:
            second_char = bank[b]
    
    # print(bank)
    # print("a:" + str(first_char) + " b:" + str(second_char))
    maxJoltage += int(str(first_char) + str(second_char))


print("Result: " + str(maxJoltage))
    