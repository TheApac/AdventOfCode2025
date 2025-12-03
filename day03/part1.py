total = 0

with open('files/full', 'r') as f:
    for line in f:
        digits = line.strip()
        max_joltage = 0
        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                joltage = int(digits[i] + digits[j])
                if joltage > max_joltage:
                    max_joltage = joltage
        total += max_joltage

print(total)