values = []
while(True):
    value = input()
    if(value == "0"):
        break
    values.append(value)

for v in values:
    print(sum([int(i) for i in list(v)]))