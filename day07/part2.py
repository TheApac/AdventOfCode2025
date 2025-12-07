cache = {}


def count_timelines(grid, row, col):
    key = (row, col)
    if key in cache:
        return cache[key]
    if row == len(grid):
        return 1
    if grid[row][col] == "^":
        total = 0
        if col > 0:
            total += count_timelines(grid, row, col - 1)
        if col < len(grid[row]) - 1:
            total += count_timelines(grid, row, col + 1)
        return total
    else:
        res = count_timelines(grid, row + 1, col)
        cache[key] = res
        return res


with open("files/full") as f:
    grid = [line.strip() for line in f if line.strip()]

start_col = grid[0].index("S")
result = count_timelines(grid, 1, start_col)
print(result)
