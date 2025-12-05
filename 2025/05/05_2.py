

ranges = []
str_ranges = []
found_blank = False

with open("input", "r") as file:
    for line in file.read().splitlines():
        if line.strip() == "":
            found_blank = True
            break
        if not found_blank:
            str_ranges.append(line)


def addRange(id_range: str):
    low_s, high_s = id_range.split("-")
    new_start = int(low_s)
    new_end = int(high_s)
    
    global ranges
    
    merged = []
    inserted = False
    
    for start, end in ranges:
        if end + 1 < new_start:
            merged.append((start, end))
        elif new_end + 1 < start:
            if not inserted:
                merged.append((new_start, new_end))
                inserted = True
            merged.append((start, end))
        else:
            new_start = min(new_start, start)
            new_end = max(new_end, end)
    
    if not inserted:
        merged.append((new_start, new_end))

    ranges = merged




for id_range in str_ranges:
    addRange(id_range)

num_ids = sum(end - start + 1 for start, end in ranges)

print("Fresh ingredients: " + str(num_ids))
