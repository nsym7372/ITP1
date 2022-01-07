import sys
input()

t, h = 0, 0
for line in sys.stdin.readlines():
    cards = list(line.split())
    if cards[0] > cards[1]:
        t += 3
    elif cards[0] < cards[1]:
        h += 3
    else:
        t += 1
        h += 1
print(f"{t} {h}")