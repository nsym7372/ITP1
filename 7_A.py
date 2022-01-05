NA = -1
scores = []
while(True):
    score = list(map(int, input().split()))
    if all(_ == NA for _ in score):
        break
    scores.append(score)

for score in scores:
    if score[0] == NA or score[1] == NA:
        print("F")
    elif score[0] + score[1] >= 80:
        print("A")
    elif 65 <= score[0] + score[1] < 80:
        print("B")
    elif 50 <= score[0] + score[1] < 65:
        print("C")
    elif 30 <= score[0] + score[1] < 50:
        grade = "C" if 50 <= score[2] else "D" 
        print(grade)
    else:
        print("F")