import math

s_n = []
s_sl = []
while(True):
    n = int(input())
    if n == 0:
        break

    s_n.append(n)
    s_sl.append(list(map(int, input().split())))

for n, sl in zip(s_n, s_sl):
    m = sum(sl) / n
    print(format( math.sqrt(sum([(s - m) ** 2 for s in sl]) / n), ".8f"))
        