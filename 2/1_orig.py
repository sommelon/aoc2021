file = open('./input.txt', 'r')
lines = file.readlines()

horiz_pos = 0
depth = 0

for line in lines:
    action, value = line.split(" ")
    if action == "forward":
        horiz_pos += int(value)
    elif action == "down":
        depth += int(value)
    elif action == "up":
        depth -= int(value)

print(horiz_pos * depth)