total = 0
nb_battery = 12
battery_per_cell = 100

with open('files/full', 'r') as f:
    for line in f:
        digits = line.strip()
        result = []
        start = 0
        for i in range(nb_battery):
            end = battery_per_cell - (nb_battery - (i + 1))
            max_digit = max(digits[start:end])
            idx = digits.index(max_digit, start, end)
            result.append(max_digit)
            start = idx + 1
        total += int(''.join(result))
print(total)