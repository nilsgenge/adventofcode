
numFreshIngredients = 0
ranges = []
ingredients = []
found_blank = False

with open("input", "r") as file:
    for line in file.read().splitlines():
        if line.strip() == "":
            found_blank = True
            continue
        if not found_blank:
            ranges.append(line)
        else:
            ingredients.append(int(line))

def inRange(id, range) -> bool:
    low_s, high_s = range.split("-")
    low = int(low_s)
    high = int(high_s)
    if id >= low and id <= high:
        return True
    return False

for ingredient in ingredients:
    for range in ranges:
        if inRange(ingredient, range):
            numFreshIngredients += 1
            # print(str(ingredient) + " - " +  range)
            break

print("Fresh ingredients: " + str(numFreshIngredients))
