_input = open('puzzle_input.txt').read().split('\n')

fabric = [[0 for j in range(1000)] for i in range(1000)]

for word in _input[:-1]:
    line = word.split()
    lt = line[2][:-1].split(',')
    left = int(lt[0])
    top = int(lt[1])
    wh = line[3].split('x')
    width = int(wh[0])
    height = int(wh[1])
    for i in range(left,left+width):
        for j in range(top, top+height):
            if fabric[i][j] == 0:
                fabric[i][j] = 1
            elif fabric[i][j] == 1:
                fabric[i][j] = 2

for word in _input[:-1]:
    line = word.split()
    lt = line[2][:-1].split(',')
    left = int(lt[0])
    top = int(lt[1])
    wh = line[3].split('x')
    width = int(wh[0])
    height = int(wh[1])
    check = True
    for i in range(left,left+width):
        for j in range(top, top+height):
            if fabric[i][j] == 2:
                check = False
    if check is True:
        print(line)
