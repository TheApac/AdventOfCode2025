with open("files/example", "r") as f:
    grid = [list(line.strip()) for line in f]

    rows = len(grid)
    cols = len(grid[0])
    accessible = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                adj_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if rows > nr >= 0 and cols > nc >= 0:
                        if grid[nr][nc] == "@":
                            adj_count += 1
                if adj_count < 4:
                    accessible += 1
    print(accessible)
