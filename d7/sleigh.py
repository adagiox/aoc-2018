import string

def get_input():
    return open('puzzle_input.txt').read()[:-1].split('\n')

def solve(steps):
    s = {k:[] for k in string.ascii_uppercase}
    for k,v in steps:
        s[v].append(k)
    not_visited = [letter for letter in string.ascii_uppercase]
    ans = ""
    while not_visited:
        n = sorted([l for l in not_visited if len(s[l]) == 0])
        print(n)
        ans += n[0]
        not_visited.remove(n[0])
        for k,v in s.items():
            if n[0] in v:
                v.remove(n[0])
    return ans

if __name__ == "__main__":
    puzzle = get_input()
    steps = []
    for line in puzzle:
        sp = line.split(' ')
        steps.append((sp[1], sp[7]))
    ans = solve(steps)
    print(ans)
