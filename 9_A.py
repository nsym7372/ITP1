w = input().lower()

count = 0
complete = False
while(complete == False):
    for t in list(input().split()):
        if t == "END_OF_TEXT":
            print(count)
            complete = True
            break
        elif (t.lower() == w):
            count += 1

            
