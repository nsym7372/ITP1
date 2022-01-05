num = int(input())

exists = {}
for i in range(0, num):
    sn = input().replace(" ", "")
    exists[sn] = 1

for s in ["S", "H", "C", "D"]:
    for n in range(0, 13):
        if(s + str(n + 1) not in exists):
            print(s, n + 1)


