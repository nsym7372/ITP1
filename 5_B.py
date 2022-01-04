hl = []
wl = []
while(True):
    h, w = map(int, input().split())
    hl.append(h)
    wl.append(w)
    if(h == 0 and w == 0):
        break

for w, h in zip(wl, hl):
    line = ""
    for i in range(0, w):
        c = "#" if (i == 0 or i == w - 1) else "."
        line += c

    for j in range(0, h):
        l = "#" * w if (j == 0 or j == h - 1 ) else line 
        print(l)

    print()
