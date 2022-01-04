while(True):
    a, b = map(str, sorted(map(int, input().split())))
    if(a == "0" and b == "0"):
        break
    print(f"{a} {b}")