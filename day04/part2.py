with open("files/full", "r") as f:
    grid = [list(line.strip()) for line in f]

rows, cols = len(grid), len(grid[0])
accessible = 0
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    to_mark = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                adj_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if rows > nr >= 0 and cols > nc >= 0:
                        adj_count += 1 if grid[nr][nc] == "@" else 0
                if adj_count < 4:
                    to_mark.append((r, c))
    accessible += len(to_mark)
    if len(to_mark) == 0:
        break
    for r, c in to_mark:
        grid[r][c] = "."
print(accessible)
