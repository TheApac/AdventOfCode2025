import re
import math

lines = []
symbols = []

with open("files/full") as f:
    all_lines = f.readlines()
    lines = [[int(n) for n in re.findall(r"\d+", line)] for line in all_lines[:-1]]
    symbols = [s for s in re.findall(r"[^\s]", all_lines[-1])]

results = [
    sum(nums) if sym == "+" else math.prod(nums)
    for nums, sym in zip(zip(*lines), symbols)
]
print(sum(results))
