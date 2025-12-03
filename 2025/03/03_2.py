
maxJoltage = 0

with open("input", "r") as file:
    banks_file = file.read()


for line in banks_file.splitlines():
    n = len(line)
    stack = []
    num_to_remove = n - 12

    for char_digit in line:
        while stack and stack[-1] < char_digit and num_to_remove > 0:
            stack.pop()
            num_to_remove -= 1
        stack.append(char_digit)
    while len(stack) > 12:
        stack.pop()

    maxJoltageBank = "".join(stack)
    maxJoltage += int(maxJoltageBank)



print("Result: " + str(maxJoltage))
