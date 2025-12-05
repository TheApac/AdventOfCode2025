from intervaltree import IntervalTree

with open("files/full", "r") as f:
    lines = [line.strip() for line in f]

i = 0
count = 0
tree = IntervalTree()

while i < len(lines) and lines[i]:
    start, end = map(int, lines[i].split("-"))
    tree[start : end + 1] = True
    i += 1
i += 1
tree.merge_overlaps()
while i < len(lines) and lines[i]:
    if tree[int(lines[i])]:
        count += 1
    i += 1

print(count)
