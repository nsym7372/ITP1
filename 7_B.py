input_set = []
while(True):
    n, x = map(int, input().split())
    if n == x == 0:
        break
    input_set.append((n, x))

for n, x in input_set:
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1): 
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    count += 1
    print(count)
