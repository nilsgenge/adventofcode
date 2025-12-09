
with open('input', 'r') as f:
    grid = [line.strip() for line in f]

R = len(grid)
C = len(grid[0])
  
sx, sy = -1, -1
for y in range(R):
    for x in range(C):
        if grid[y][x] == 'S':
            sx, sy = x, y
    
dp = [[0] * C for _ in range(R)]
dp[sy][sx] = 1
  
for y in range(sy, R - 1):
    for x in range(C):
        if dp[y][x] > 0:
            cell_below = grid[y + 1][x]
            if cell_below == '.':
                dp[y + 1][x] += dp[y][x]
            elif cell_below == '^':
                if x - 1 >= 0:
                    dp[y + 1][x - 1] += dp[y][x]
                if x + 1 < C:
                    dp[y + 1][x + 1] += dp[y][x]
    
result = sum(dp[R - 1][x] for x in range(C))
print("RESULT: " + str(result))
