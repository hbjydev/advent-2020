input = []
target = 2020

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

for i in range(0, len(input)):
    input[i] = int(input[i])

for i, number in enumerate(input[:-1]):
    complementary = target - number
    if complementary in input[i+1:]:
        print(complementary * number)
        break
