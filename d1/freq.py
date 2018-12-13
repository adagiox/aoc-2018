_input = open('freq_input.txt').read().strip().split()
freqs = {0:1}
freq = 0
running = True
while running:
    for num in _input:
        freq += int(num)
        check = freqs.get(freq, 0)
        if check == 0:
            freqs[freq] = 1
        else:
            print(freq)
            running = False
            break

print("Done.")
