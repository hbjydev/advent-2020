input = []

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

passes = 0
fails = 0

for line in input:
    info = str.split(line, ': ')
    policy = str.split(info[0], ' ')
    password = info[1]

    chara = policy[1]
    between = str.split(policy[0], '-')
    between[0] = int(between[0])
    between[1] = int(between[1])

    count = 0
    for character in list(password):
        if character == chara:
            count = count + 1

    if (count >= between[0]) and (count <= between[1]):
        passes += 1
    else:
        fails += 1

print(f'Passes: {passes}')
print(f'Fails: {fails}')
