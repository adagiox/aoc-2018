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
            if grid[i][j][0][1] != grid[i][j][1][1]:
                grid2[i][j] = grid[i][j][0][0]
    skip = []
    for i in range(ROW_DIM):
        for j in range(COL_DIM):
            if i == 0 or j == 0 or i == ROW_DIM-1 or j == COL_DIM-1:
                num = grid2[i][j]
                if num not in skip and num != '.':
                    skip.append(num)
    largest = defaultdict(int)
    for i in range(ROW_DIM):
        for j in range(COL_DIM):
            if grid2[i][j] not in skip:
                largest[grid2[i][j]] += 1
    print(largest)
    print(f"Point: {max(largest, key=largest.get)}\nArea: {largest[max(largest, key=largest.get)]}")

if __name__ == "__main__":
    grid = [[[] for j in range(COL_DIM)] for i in range(ROW_DIM)]
    grid2 = [['.' for j in range(COL_DIM)] for i in range(ROW_DIM)]
    coords = setup_puzzle()
    grid = dist_grid(coords)
    largest_area(grid, grid2)
