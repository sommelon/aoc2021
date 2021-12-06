import itertools

file = open('./input.txt', 'r')
lines = file.readlines()
lines = [line.strip().replace(' ', '').split('->') for line in lines]
file.close()
diagram = {} # {'x,y': count}

def get_coords_in_range(coord1, coord2):
    return [coord for coord in range(min(coord1, coord2), max(coord1, coord2) + 1)]


for line in lines:
    left, right = line[0].split(','), line[1].split(',')
    x1, x2 = int(left[0]), int(right[0])
    y1, y2 = int(left[1]), int(right[1])

    if x1 != x2 and y1 != y2:
        continue

    xs = get_coords_in_range(x1, x2)
    ys = get_coords_in_range(y1, y2)

    for coord in itertools.zip_longest(xs, ys, fillvalue=x1 if len(xs) < len(ys) else y1):
        diagram[coord] = diagram.get(coord, 0) + 1

count = 0
for k, v in diagram.items():
    if v >= 2:
        count += 1

print(count) #5835