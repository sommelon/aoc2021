file = open('./input.txt', 'r')
lines = file.readlines()

ones = [0] * (len(lines[0]) - 1)

for line in lines:
    ints = [int(c) for c in line if c != '\n']
    for i in range(len(ones)):
        ones[i] += ints[i]

gamma = [int(ones[i] > len(lines) / 2) for i in range(len(ones))]
epsilon = [abs(e - 1) for e in gamma]
gamma = map(str, gamma)
epsilon = map(str, epsilon)

print(int("".join(gamma), 2) * int("".join(epsilon), 2)) #775304