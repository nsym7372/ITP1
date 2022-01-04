import sys
W, H, x, y, r = map(int, input().split())

if(0 < x < W):
    if(x - r < 0 or x + r > W):
        print("No")
        sys.exit()
else:
    print("No")
    sys.exit()

if(0 < y < H):
    if(y - r < 0 or y + r > H):
        print("No")
        sys.exit()
else:
    print("No")
    sys.exit()

print('Yes')