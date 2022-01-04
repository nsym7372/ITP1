n = int(input())
result = []
def call(n):

    for i in range(1, n + 1):
        if(is_valid(i)):
            result.append(f" {i}")

def is_valid(i):
    if(i % 3 == 0 or i % 10 == 3):
        return True
    return include3(i)

def include3(i):
    if(i % 10 == 3):
        return True
    elif(i // 10 == 0):
        return False
    else:
        return include3(i // 10)


call(n)
print("".join(result))