words = []
numbers = []

num_list = []
while(True):
    s_in = input()
    if s_in == "-":
        numbers.append(num_list)
        break
    elif s_in.isalpha():
        if len(num_list) != 0:
            numbers.append(num_list)
            num_list = []
        words.append(s_in)
    else:
        num_list.append(int(s_in))

for w, n_list in zip(words, numbers):
    n_list.pop(0)
    for i in n_list:
        w = w[i:] + w[:i]

    print(w)
