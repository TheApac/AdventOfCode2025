with open("files/full", "r") as f:
    grid = [list(line.strip()) for line in f]

    rows, cols = len(grid), len(grid[0])
    accessible = 0
    last_accessible = -1
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while True:
        needs_restart = False
        last_accessible = accessible
        to_mark = []
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
                        to_mark.append((r, c))
                        needs_restart = True
        if not needs_restart:
            break
        for r, c in to_mark:
            grid[r][c] = "."
    print(accessible)
