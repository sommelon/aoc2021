file = open('./input.txt', 'r')
lines = list(map(int, file.readlines()))
increased_count = sum(1 for i in range(1, len(lines)) if lines[i] > lines[i-1])
print(increased_count) #1688