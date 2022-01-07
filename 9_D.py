s_in = input()
calls = int(input())

def d_print(word, start, end, blank):
    print(word[start:end])
    return word

def d_replace(word, start, end, r_word):
    return word[:start] + r_word + word[end:]

def d_reverse(word, start, end, blank):
    return word[:start] + "".join(reversed(word[start:end])) + word[end:]

for _ in range(calls):
    signs = list(input().split())
    if len(signs) == 3:
        signs.append("")
    end = int(signs[2]) + 1
    s_in = eval(f'd_{signs[0]}("{s_in}", {signs[1]}, {end}, "{signs[3]}")')