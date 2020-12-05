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
    positions = str.split(policy[0], '-')
    positions[0] = int(positions[0])
    positions[1] = int(positions[1])

    if password[positions[0] - 1] == chara and password[positions[1] - 1] != chara:
        passes += 1
    elif password[positions[0] - 1] != chara and password[positions[1] - 1] == chara:
        passes += 1
    else:
        fails += 1

print(f'Passes: {passes}')
print(f'Fails: {fails}')
