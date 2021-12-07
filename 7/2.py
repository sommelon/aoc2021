file = open('./input.txt', 'r')
positions = [int(num) for num in file.readline().split(',')]
file.close()

def cum_sum(num):
    partial_sum = 0
    for i in range(1, num + 1):
        partial_sum += i
    return partial_sum

best_position = 0
best_fuel_consumption = cum_sum(sum(positions))

for end_pos in range(min(positions), max(positions) + 1):
    fuel_sum = 0
    for pos in positions:
        fuel_sum += cum_sum(abs(pos - end_pos))
        if fuel_sum > best_fuel_consumption:
            break
    if fuel_sum < best_fuel_consumption:
        best_fuel_consumption, best_position = fuel_sum, end_pos

print(best_fuel_consumption) #96361606