import itertools

file = open('./input.txt', 'r')
lines = file.readlines()
lines = [line.strip().replace(' ', '').split('->') for line in lines]
file.close()
diagram = {} # {'x,y': count}

def get_coords_in_range(coord1, coord2):
    coord2, coord1 = (coord1, coord2) if coord1 > coord2 else (coord2, coord1)
    return [coord for coord in range(coord1, coord2 + 1)]


for line in lines:
    left = line[0].split(',')
    right = line[1].split(',')
    x1, x2 = int(left[0]), int(right[0])
    y1, y2 = int(left[1]), int(right[1])

    if x1 != x2 and y1 != y2:
        continue

    xs = get_coords_in_range(x1, x2)
    ys = get_coords_in_range(y1, y2)

    for coord in itertools.zip_longest(xs, ys, fillvalue=x1 if len(xs) < len(ys) else y1):
        coord_str = f'{coord[0]},{coord[1]}'
        coord_count = diagram.get(coord_str, 0)
        diagram[coord_str] = coord_count + 1

count = 0
for k, v in diagram.items():
    if v >= 2:
        count += 1

print(count) #5835