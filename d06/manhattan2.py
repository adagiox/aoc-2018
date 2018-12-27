from collections import defaultdict

ROW_DIM = 400
COL_DIM = 400

def setup_puzzle():
    _input = open('puzzle_input.txt').read()[:-1]
    _input = _input.split('\n')
    return([tuple(list(map(int, line.split(', ')))) for line in _input])

def dist_grid(coords):
    for i in range(ROW_DIM):
        for j in range(COL_DIM):
            coord = 0
            for col, row in coords:
                grid[i][j].append((coord, abs(col - j) + abs(row - i)))
                coord += 1
    return grid

def largest_area(grid, grid2):
    for i in range(ROW_DIM):
        for j in range(COL_DIM):
            grid[i][j] = sorted(grid[i][j], key = lambda c: c[1])
    for i in range(ROW_DIM):
        for j in range(COL_DIM):
            s = 0
            for s2 in grid[i][j]:
                s += s2[1]
            grid2[i][j] = s
    area = 0
    for i in range(ROW_DIM):
        for j in range(COL_DIM):
            if grid2[i][j] < 10000:
                area += 1
    print(area)

if __name__ == "__main__":
    grid = [[[] for j in range(COL_DIM)] for i in range(ROW_DIM)]
    grid2 = [['.' for j in range(COL_DIM)] for i in range(ROW_DIM)]
    coords = setup_puzzle()
    grid = dist_grid(coords)
    largest_area(grid, grid2)
