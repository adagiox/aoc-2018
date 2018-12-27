_input = open('puzzle_input.txt').read()[:-1]
orig = _input
alpha = []
for i in range(26):
    polymer = orig
    polymer = polymer.replace(chr(i+65), '')
    polymer = polymer.replace(chr(i+97), '')
    while True:
        for i in range(len(polymer)-1):
            if polymer[i].lower() == polymer[i+1].lower():
                if polymer[i] != polymer[i+1]:
                    #print(polymer[i-4:i+4])
                    polymer = polymer[:i] + polymer[i+2:]
                    #print(polymer[i-4:i+4])
                    break
        else:
            break
    alpha.append(len(polymer))
print("Done")
#print(polymer)
print(alpha)
print(max(alpha))
