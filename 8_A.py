s_in = input()

result = []
for s in s_in:
    if s.isupper():
        result.append(s.lower())
    elif s.islower():
        result.append(s.upper())
    else:
        result.append(s)

print("".join(result))
        