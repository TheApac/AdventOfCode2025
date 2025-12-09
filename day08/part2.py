from math import prod

boxes = []
with open('files/full') as f:
    for line in f:
        parts = [int(x) for x in line.strip().split(',')]
        boxes.append(tuple(parts))

circuits = []

n = len(boxes)
pairs = []
for i in range(n):
    x1, y1, z1 = boxes[i]
    for j in range(i + 1, n):
        x2, y2, z2 = boxes[j]
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        dist2 = dx * dx + dy * dy + dz * dz
        pairs.append((dist2, i, j))

pairs.sort()

last_pair = None
for k in range(len(pairs)):
    d, i, j = pairs[k]
    a = boxes[i]
    b = boxes[j]

    idx_circuit_a = next((idx for idx, c in enumerate(circuits) if a in c), None)
    idx_circuit_b = next((idx for idx, c in enumerate(circuits) if b in c), None)

    if idx_circuit_a is None and idx_circuit_b is None:
        circuits.append({a, b})
        last_pair = (boxes[i], boxes[j])
    elif idx_circuit_a is not None and idx_circuit_b is None:
        circuits[idx_circuit_a].add(b)
        last_pair = (boxes[i], boxes[j])
    elif idx_circuit_a is None and idx_circuit_b is not None:
        circuits[idx_circuit_b].add(a)
        last_pair = (boxes[i], boxes[j])
    elif idx_circuit_a == idx_circuit_b:
        pass
    else:
        circuits[idx_circuit_a].update(circuits[idx_circuit_b])
        del circuits[idx_circuit_b]
        last_pair = (boxes[i], boxes[j])

    if len(circuits) == 1 and len(circuits[0]) == n:
        break

x1 = last_pair[0][0]
x2 = last_pair[1][0]
result = x1 * x2
print(result)