file = open('./input.txt', 'r')
timers = [int(num) for num in file.read().split(',')]
file.close()

for day in range(80):
    for i in range(len(timers)):
        if timers[i] == 0:
            timers[i] = 6
            timers.append(8)
        else:
            timers[i] -= 1

print(len(timers)) #372984