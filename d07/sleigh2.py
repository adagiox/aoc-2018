import string

def get_input():
    return open('puzzle_input.txt').read()[:-1].split('\n')

def solve(steps):
    s = {k:[] for k in string.ascii_uppercase}
    for k,v in steps:
        s[v].append(k)
    not_visited = [letter for letter in string.ascii_uppercase]
    ans = 0
    workers = [["",0] for i in range(5)]
    while not_visited or [i for i in range(len(workers)) if workers[i][1] != 0]:
        n = sorted([l for l in not_visited if len(s[l]) == 0])
        workers_ready = [i for i in range(len(workers)) if workers[i][1] == 0]
        while workers_ready and n:
            w = workers_ready.pop()
            workers[w][0] = n[0]
            workers[w][1] = ord(n[0])-4
            not_visited.remove(n.pop(0))
        ans += 1
        for i in range(len(workers)):
            if workers[i][1] == 1:
                for k,v in s.items():
                    if workers[i][0] in v:
                        v.remove(workers[i][0])
                workers[i][1] = 0
            elif workers[i][1] > 0: 
                workers[i][1] -= 1
    return ans

if __name__ == "__main__":
    puzzle = get_input()
    steps = []
    for line in puzzle:
        sp = line.split(' ')
        steps.append((sp[1], sp[7]))
    ans = solve(steps)
    print(ans)
