from collections import defaultdict
_input = open('puzzle_input.txt').read().strip().split()

two = []
three = []

for _id in _input:
    check = defaultdict(int)
    for ch in _id:
        check[ch] += 1
    twice = 0
    for k,v in check.items():
        if v == 2:
            twice += 1
            break
    two.append(twice)

for _id in _input:
    check = defaultdict(int)
    for ch in _id:
        check[ch] += 1
    thrice = 0
    for k,v in check.items():
        if v == 3:
            thrice += 1
            break
    three.append(thrice)

total_twice = 0
total_thrice = 0

for count in two:
    total_twice += count

for count in three:
    total_thrice += count

print(total_twice *total_thrice)
