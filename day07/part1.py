with open("files/full") as f:
    grid = [line.strip() for line in f if line.strip()]

start_col = grid[0].index("S")
splits = set()
beams = set([(0, start_col)])

while beams:
    row, col = beams.pop()
    while row < len(grid):
        if grid[row][col] == "^":
            splits.add((row, col))
            if col > 0:
                beams.add((row, col - 1))
            if col < len(grid[row]) - 1:
                beams.add((row, col + 1))
            break
        row += 1

print(len(splits))
