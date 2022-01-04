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
        c = "#" if (i % 2 == 0) else "."
        line += c

    for j in range(0, h):
        print(line)
        line = line.replace(".", "-").replace("#", ".").replace("-", "#")
        
    print()
