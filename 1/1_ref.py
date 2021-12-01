file = open('./input.txt', 'r')
lines = file.readlines()

lines = list(map(int, lines))
increased_count = sum(1 for i in range(1, len(lines)) if lines[i] > lines[i-1])
print(increased_count) #1688