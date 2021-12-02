import itertools

file = open('./input.txt', 'r')
lines = list(map(int, file.readlines()))
sliding_windows = itertools.zip_longest(lines, lines[1:], lines[2:], fillvalue=0)
window_sums = list(map(sum, sliding_windows))
increased_count = sum(1 for i in range(1, len(window_sums)) if window_sums[i] > window_sums[i - 1])
print(increased_count) #1728