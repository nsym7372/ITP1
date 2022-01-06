import sys
import string
result = {}
for a in list(string.ascii_lowercase):
    result[a] = 0

str_in = list(sys.stdin.read().lower())

for s in str_in:
    if s in result:
        result[s] += 1

for k, v in sorted(result.items()):
    print(f"{k} : {v}")
