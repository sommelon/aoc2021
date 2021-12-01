file = open('./input.txt', 'r')
lines = file.readlines()

lines = list(map(int, lines))
prev_sum = lines[0] + lines[1] + lines[2]
increased_count = 0
for i in range(1, len(lines)-2):
    window_sum = lines[i] + lines[i+1] + lines[i+2]
    if window_sum > prev_sum:
        increased_count += 1
    prev_sum = window_sum

print(increased_count) #1728