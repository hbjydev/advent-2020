input = []

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

move_x = [ 1, 3, 5, 7, 1 ]
move_y = [ 1, 1, 1, 1, 2 ]

trees_oa = 1

for i in range(0, len(move_x)):
    y = 0 # Vertical Position (used for progress)
    x = 0 # Horizonal Position (used for scroll tracking)
    trees = 0 # Trees collided with
    finish = False

    while finish != True:
        position = input[y][x]
        if position == '#':
            trees += 1

        if (x + move_x[i]) >= len(input[0]):
            x = (x + move_x[i]) - len(input[0])
        else:
            x += move_x[i]

        if y + move_y[i] >= len(input):
            finish = True
        else:
            y += move_y[i]

    print(f'x:{move_x[i]} -- y:{move_y[i]} -- trees:{trees}')

    trees_oa = trees_oa * trees

print(f'Tree product from all {len(move_x)} patterns: {trees_oa}')
