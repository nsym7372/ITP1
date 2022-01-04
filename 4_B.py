import math
r = float(input())

area = format(r * r * math.pi, ".6f")
cir = format(2 * r * math.pi, ".6f")
print(f"{area} {cir}")