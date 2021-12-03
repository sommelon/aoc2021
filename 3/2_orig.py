import functools

file = open('./input.txt', 'r')
lines = file.readlines()

def get_rating(lines, func):
    rating = lines
    for i in range(len(lines[0])):
        ones = 0
        for line in rating:
            ones += int(line[i])

        if func(ones, len(rating) / 2):
            num = '1'
        else:
            num = '0'

        rating = [line for line in rating if line[i] == num]
        if len(rating) == 1:
            return int(rating[0], 2)

get_oxygen_rating = functools.partial(get_rating, lines, lambda ones, length: ones >= length)
get_co2_rating = functools.partial(get_rating, lines, lambda ones, length: ones < length)

print(get_oxygen_rating() * get_co2_rating()) #1370737