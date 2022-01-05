datas = int(input())

rooms = [[[0 for i in range(0, 10)] for j in range(0, 3)] for k in range(0, 4)]
for _ in range(0, datas):
    b, f, r, v = map(int, input().split())
    rooms[b - 1][f - 1][r - 1] += v

for i, r in enumerate(rooms):
    for f in r:
        print(" ", end="")
        print(*f)
    if i != 3:
        print("#" * 20)