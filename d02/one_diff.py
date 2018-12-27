import sys
_input = open('puzzle_input.txt').read().strip().split()

dists = {}

for i in range(len(_input)):
    dists[_input[i]] = {}
    for _id in _input[i+1:]:
        dists[_input[i]][_id] = sum(el1 != el2 for el1, el2 in zip(_input[i], _id))


for k1,v1 in dists.items():
    for k2,v2 in v1.items():
        if v2 == 1:
            print(k1)
            print(k2)
            sys.exit()
        
