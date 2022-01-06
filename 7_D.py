n_in, m_in, l_in = list(map(int, input().split()))

left = []
for i in range(n_in):
    left.append(list(map(int, input().split())))

right = []
for j in range(m_in):
    right.append(list(map(int, input().split())))

ans = []
for l in range(n_in):
    ans_line = []
    for r in range(l_in):
        answer = 0
        for m in range(m_in):
            answer += left[l][m] * right[m][r]
        ans_line.append(answer)
    ans.append(ans_line)

for a in ans:
    print(*a)