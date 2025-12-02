counter = 50
zeroCounter = 0

with open('files/full', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        letter = line[0]
        number = int(line[1:])
        if letter == 'L':
            if counter == 0:
                zeroCounter -= 1
            counter -= number
            zeroCounter -= counter // 100
            if counter % 100 == 0:
                zeroCounter += 1
        elif letter == 'R':
            counter += number
            zeroCounter += counter // 100
        counter %= 100

print(zeroCounter)