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
            counter = (counter - number) % 100
        elif letter == 'R':
            counter = (counter + number) % 100
        if counter == 0:
            zeroCounter += 1

print(zeroCounter)