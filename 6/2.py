from collections import deque

file = open('./input.txt', 'r')
timers = [int(num) for num in file.readline().split(',')]
file.close()
fish_count = deque([timers.count(i) if i in timers else 0 for i in range(9)])

for day in range(256):
    fish_count[7] += fish_count[0]
    fish_count.rotate(-1)

print(sum(fish_count)) #1681503251694