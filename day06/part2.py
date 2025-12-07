import re
import math

with open("files/full") as f:
    all_lines = f.readlines()
    digit_lines = [
        line.rstrip("\n") for line in all_lines[:-1] if re.search(r"\d", line)
    ]
    symbol_line = all_lines[-1]

symbols = [s for s in re.findall(r"[^\s]", symbol_line)]

num_cols = max(len(row) for row in digit_lines)
merged = []
temp = []
for col in range(num_cols):
    col_vals = [row[col] if col < len(row) else "" for row in digit_lines]
    if all(c.isspace() for c in col_vals):
        merged.append(temp)
        temp = []
        continue
    temp.append(int("".join(col_vals)))
merged.append(temp)

results = [
    sum(nums) if sym == "+" else math.prod(nums) for nums, sym in zip(merged, symbols)
]
print(sum(results))
