file = open('./input.txt', 'r')
lines = file.readlines()

aim = 0
horiz_pos = 0
depth = 0

for line in lines:
    action, value = line.split(" ")
    value = int(value)
    if action == "forward":
        horiz_pos += value
        depth += aim * value
    elif action == "down":
        aim += value
    elif action == "up":
        aim -= value

print(horiz_pos * depth)