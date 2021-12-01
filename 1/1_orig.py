file = open('./input.txt', 'r')
lines = file.readlines()

prev_measurement = int(lines[0])
increased_count = 0
for line in lines:
    iLine = int(line)
    if iLine > prev_measurement:
        increased_count += 1
    prev_measurement = iLine

print(increased_count) #1688