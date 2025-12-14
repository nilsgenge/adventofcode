import math
import heapq

boxes = []
result = 0

with open("input", "r") as file:
    for line in file.read().splitlines():
        x, y, z = line.split(",")
        boxes.append((int(x), int(y), int(z)))

parent = list(range(len(boxes)))
rank = [0] * len(boxes)


def calculateDistance(p1, p2):
    tmp = abs(p1[0] - p2[0])**2 + abs(p1[1] - p2[1])**2 + abs(p1[2] - p2[2])**2
    return math.sqrt(tmp)

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(a,b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return False
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1
    return True

heap = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distance = calculateDistance(boxes[i], boxes[j])
        heapq.heappush(heap, (distance, i, j))

last_i, last_j = 0, 0
while heap:
    d, i, j = heapq.heappop(heap)
    if union(i,j):
        last_i, last_j = i, j
        roots = {find(u) for u in range(len(boxes))}
        if len(roots) == 1:
            break

result = boxes[last_i][0] * boxes[last_j][0]

print("RESULT: " + str(result))
