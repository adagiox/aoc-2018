
def get_input(_input):
    return open(_input).read().split('\n')[:-1]

def solve(puzzle):
    points = [list(map(int, [line[10:16],line[18:24]])) for line in puzzle]
    velocity = [list(map(int, [line[36:38],line[40:42]])) for line in puzzle]
    bounds = []
    for i in range(10375):
        bounds.append(bound(points))
        points = tick(points, velocity)
        if i > 10350:
            print(min(bounds), bounds.index(min(bounds)))
            plot(points, i)

def plot(points, num):
    x_min = min(points, key = lambda p: p[0])[0]
    x_max = max(points, key = lambda p: p[0])[0]
    y_min = min(points, key = lambda p: p[1])[1]
    y_max = max(points, key = lambda p: p[1])[1]
    grid = [['.' for j in range(y_max * 2)] for i in range(x_max * 2)]
    for p in points:
        grid[p[0]][p[1]] = '#'
    with open(f'output{num}.txt', 'w') as f:
        for row in grid:
            for c in row:
                f.write(c)
            f.write('\n')

def tick(points, velocity):
    for i in range(len(points)):
        points[i][0] = points[i][0] + velocity[i][0]
        points[i][1] = points[i][1] + velocity[i][1]
    return points

def bound(points):
    x_min = min(points, key = lambda p: p[0])[0]
    x_max = max(points, key = lambda p: p[0])[0]
    y_min = min(points, key = lambda p: p[1])[1]
    y_max = max(points, key = lambda p: p[1])[1]
    return( ( abs(x_min) + abs(x_max) ) * ( abs(y_min) + abs(y_max) ) )

if __name__ == "__main__":
    puzzle = get_input("puzzle_input.txt")
    solve(puzzle)
