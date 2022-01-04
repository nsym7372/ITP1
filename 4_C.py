while(True):
    sa, op ,sb = map(str, input().split())
    a, b = map(int, [sa, sb])
    if(op == "?"):
        break
    elif(op == "+"):
        print(a + b)
    elif(op == "-"):
        print(a - b)
    elif(op == "*"):
        print(a * b)
    else:
        print(a // b)
