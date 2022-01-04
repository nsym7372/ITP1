a, b, c = map(int, input().split())

divisor = []
for i in range(1, c + 1):
    if(c % i == 0):
        divisor.append(i)

result = 0
for j in range(a, b + 1):
    if(j in divisor):
        result += 1

print(result)