from intervaltree import IntervalTree

with open("files/full", "r") as f:
    lines = [line.strip() for line in f]

i = 0
tree = IntervalTree()

while i < len(lines) and lines[i]:
    start, end = map(int, lines[i].split("-"))
    tree[start : end + 1] = True
    i += 1

tree.merge_overlaps()
fresh_count = sum(it.end - it.begin for it in tree)
print(fresh_count)
