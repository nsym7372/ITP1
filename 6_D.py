n, m = map(int, input().split())

matrix = []
for ni in range(n):
    m_list = list(map(int, input().split()))
    matrix.append(m_list)

vector = []
for vi in range(m):
    vector.append(int(input()))

for i, m_row in enumerate(matrix):
    row_result = 0
    for p in range(0, m):
        row_result += m_row[p] * vector[p]
    print(row_result)
