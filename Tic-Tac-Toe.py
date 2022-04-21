import sys

variable = 'X' or 'O'


# Reset board
def reset():
    global variable
    variable = 'X'
    vol = [[], [], []]
    for cell in vol:
        i = 0
        while i < 3:
            cell.append('_')
            i += 1
    return vol


# Print graphic board
def matrix(data):
    vol = [[], [], []]
    i = 0
    for cell in data:
        j = 0
        while j < 3:
            if cell[j] == '_':
                vol[i].append(' ')
            else:
                vol[i].append(cell[j])
            j += 1
        i += 1
    return f"""---------
| {vol[0][0]} {vol[0][1]} {vol[0][2]} |
| {vol[1][0]} {vol[1][1]} {vol[1][2]} |
| {vol[2][0]} {vol[2][1]} {vol[2][2]} |
---------"""


# Input coordinate
def user():
    try:
        x, y = input('Enter the coordinates: ').split()
        return x, y
    except ValueError:
        print('Not enough data!')


# Check input coordinate
def check_input(data, coordinate):
    x = coordinate[0]
    y = coordinate[1]
    if (x.isdecimal() is False) or (y.isdecimal() is False):
        return 'You should enter numbers!'
    elif (int(x) not in range(1, 4, 1)) or (int(y) not in range(1, 4, 1)):
        return 'Coordinates should be from 1 to 3!'
    elif data[int(x) - 1][int(y) - 1] != '_':
        return 'This cell is occupied! Choose another one!'
    else:
        return 'Ok'


# Record coordinate board
def register(data, coordinate, value):
    x = int(coordinate[0]) - 1
    y = int(coordinate[1]) - 1
    data[x][y] = value
    global variable
    if value == 'X':
        variable = 'O'
    elif value == 'O':
        variable = 'X'
    else:
        print('Error global variable')
    return data


# Value register
def value_input(check, data, coordinate, value):
    if check == 'Ok':
        return register(data, coordinate, value)


# Check wins
def wins(data):
    x1 = data[0][0] == data[0][1] == data[0][2] == 'X'
    x2 = data[1][0] == data[1][1] == data[1][2] == 'X'
    x3 = data[2][0] == data[2][1] == data[2][2] == 'X'
    x4 = data[0][0] == data[1][0] == data[2][0] == 'X'
    x5 = data[0][1] == data[1][1] == data[2][1] == 'X'
    x6 = data[0][2] == data[1][2] == data[2][2] == 'X'
    x7 = data[0][0] == data[1][1] == data[2][2] == 'X'
    x8 = data[0][2] == data[1][1] == data[2][0] == 'X'

    y1 = data[0][0] == data[0][1] == data[0][2] == 'O'
    y2 = data[1][0] == data[1][1] == data[1][2] == 'O'
    y3 = data[2][0] == data[2][1] == data[2][2] == 'O'
    y4 = data[0][0] == data[1][0] == data[2][0] == 'O'
    y5 = data[0][1] == data[1][1] == data[2][1] == 'O'
    y6 = data[0][2] == data[1][2] == data[2][2] == 'O'
    y7 = data[0][0] == data[1][1] == data[2][2] == 'O'
    y8 = data[0][2] == data[1][1] == data[2][0] == 'O'

    if x1 or x2 or x3 or x4 or x5 or x6 or x7 or x8 is True:
        return 'X wins'
    elif y1 or y2 or y3 or y4 or y5 or y6 or y7 or y8 is True:
        return 'O wins'
    else:
        return 'Ok'


# Check draw
def draw(data):
    l1 = (data[0].count('X') + data[0].count('O')) == 3
    l2 = (data[1].count('X') + data[1].count('O')) == 3
    l3 = (data[2].count('X') + data[2].count('O')) == 3
    if l1 and l2 and l3 is True:
        return 'Draw'
    else:
        return 'Ok'


play = reset()
print(matrix(play))
while True:
    input_user = user()
    if input_user is None:
        continue
    else:
        check_user = check_input(play, input_user)
        if check_user == 'Ok':
            play = register(play, input_user, variable)
            print(matrix(play))
            if wins(play) == 'Ok':
                if draw(play) == 'Ok':
                    continue
                else:
                    print(draw(play))
                    sys.exit(0)
            else:
                print(wins(play))
                sys.exit(0)
        else:
            print(check_user)
