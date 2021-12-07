file = open('./input.txt', 'r')
positions = [int(num) for num in file.readline().split(',')]
file.close()

best_position = 0
best_fuel_consumption = sum(positions)

for end_pos in range(min(positions), max(positions) + 1):
    fuel_sum = 0
    for pos in positions:
        fuel_sum += abs(pos - end_pos)
    if fuel_sum < best_fuel_consumption:
        best_fuel_consumption, best_position = fuel_sum, end_pos

print(best_fuel_consumption) #345197