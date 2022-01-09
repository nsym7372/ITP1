dim = int(input())
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))


def distance(p):
    return  format( sum([abs(xl[i] - yl[i]) ** p for i in range(len(xl))]) ** (1 / p), ".6f")

print(distance(1))
print(distance(2))
print(distance(3))

print(format( max([abs(xl[i] - yl[i]) for i in range(len(xl))]), ".6f"))