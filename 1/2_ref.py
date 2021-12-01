import itertools

file = open('./input.txt', 'r')
lines = file.readlines()

lines = list(map(int, lines))
sliding_windows = itertools.zip_longest(lines[::1], lines[1::1], lines[2::1], fillvalue=0)
window_sums = list(map(sum, sliding_windows))
increased_count = sum(1 for i in range(1, len(window_sums)) if window_sums[i] > window_sums[i-1])
print(increased_count) #1728