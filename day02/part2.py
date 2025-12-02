with open('files/full', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        invalid_ids = []
        ranges = line.strip().split(',')
        for r in ranges:
            start, end = r.split('-')
            start, end = int(start), int(end)
            for i in range(start, end + 1):
                s = str(i)
                for size in range(1, len(s) // 2 + 1):
                    if len(s) % size == 0:
                        if s == s[:size] * (len(s) // size):
                            invalid_ids.append(i)
                            break
    print(sum(invalid_ids))