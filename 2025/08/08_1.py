import math
import heapq

boxes = []

with open("input", "r") as file:
    for line in file.read().splitlines():
        x, y, z = line.split(",")
        boxes.append((int(x), int(y), int(z)))

parent = list(range(len(boxes)))
rank = [0] * len(boxes)
boxesToProcess = 1000


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
        return
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

heap = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distance = calculateDistance(boxes[i], boxes[j])
        heapq.heappush(heap, (distance, i, j))

for _ in range(boxesToProcess):
    d, i, j = heapq.heappop(heap)
    union(i, j)


circuit_sizes = {}
for u in range(len(boxes)):
    root = find(u)
    if root in circuit_sizes:
        circuit_sizes[root] += 1
    else:
        circuit_sizes[root] = 1

circuit_sizes_sorted = sorted(circuit_sizes.values(), reverse=True)

result = 1
for size in circuit_sizes_sorted[:3]:
    result *= size

print("RESULT: " + str(result))
