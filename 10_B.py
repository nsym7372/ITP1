import math
a, b, C = map(int, input().split())

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * float(math.cos(math.radians(C))))
S = 0.5 * a * b * float(math.sin(math.radians(C)))
print(format(S, ".8f"))
print(format(a + b + c, ".8f"))
print(format(2 * S / a, ".8f"))

