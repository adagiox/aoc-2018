from datetime import datetime, timedelta

puzzle = open('puzzle_input.txt').read().split('\n')[:-1]

schedule = {}

puzzle = sorted(puzzle, key=lambda g: datetime(year=int(g[1:5]), month=int(g[6:8]), day=int(g[9:11]), hour=int(g[12:14]), minute=int(g[15:17])))

current_guard = 0
for entry in puzzle:
    if '#' in entry:
        current_guard = entry.split(' ')[3][1:]
        if current_guard not in schedule:
            schedule[current_guard] = {"total_minutes":0,"schedule":[]}
    else:
        d = datetime(year=int(entry[1:5]), month=int(entry[6:8]), day=int(entry[9:11]), hour=int(entry[12:14]), minute=int(entry[15:17]))
        if d.hour == 23:
            d.hour = 0
            d.minute = 0
        sleep = True
        if entry[19] == 'w':
            sleep = False
        schedule[current_guard]["schedule"].append((d, sleep))

total_mins = {}

for k,v in schedule.items():
    total_min = 0
    for i in range(0, len(v["schedule"]), 2):
        diff = v["schedule"][i+1][0] - v["schedule"][i][0]
        diff = int(diff.total_seconds() / 60)
        total_min += diff
        if k not in total_mins:
            total_mins[k] = [0 for _ in range(60)]
        for j in range(v["schedule"][i][0].minute, v["schedule"][i][0].minute + diff):
            total_mins[k][j] += 1
    v["total_minutes"] = total_min

m = 0
m_l = []
m_v = 0
m_i = 0

for k,v in total_mins.items():
    if max(v) > m_v:
        m_v = max(v)
        m = k
        m_l = v
        m_i = v.index(m_v)

print(m)
print(m_v)
print(m_i)
print(m_l)
print(m_i * int(m))

import sys
sys.exit()

sleepiest = '431'
for k,v in schedule.items():
    if v["total_minutes"] > schedule[sleepiest]["total_minutes"]:
        sleepiest = k

sleep_mins = [0 for i in range(60)]

for i in range(0, len(schedule[sleepiest]["schedule"]), 2):
    diff = schedule[sleepiest]["schedule"][i+1][0] - schedule[sleepiest]["schedule"][i][0]
    diff = int(diff.total_seconds() / 60)
    for j in range(schedule[sleepiest]["schedule"][i][0].minute, schedule[sleepiest]["schedule"][i][0].minute+diff):
        sleep_mins[j] += 1
print(int(sleepiest) * sleep_mins.index(max(sleep_mins)))
