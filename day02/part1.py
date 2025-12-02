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
                half = len(s) // 2
                if len(s) % 2 == 0 and s[:half] == s[half:]:
                    invalid_ids.append(i)
    print(sum(invalid_ids))