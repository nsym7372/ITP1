r_in, c_in = map(int, input().split())

matrix = []

for i in range(r_in):
    matrix.append(list(map(int, input().split())))

for row in matrix:
    row.append(sum(row))

col_sum = []
for col_i in range(c_in + 1):
    s = 0
    for row in matrix:
        s += row[col_i]
    col_sum.append(s)

matrix.append(col_sum)

for r in matrix:
    print(*r)