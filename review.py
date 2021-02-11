def stringsplit(s):
    odd_string = ""
    even_string = ""
    for i in range(0, len(s)):
        if (i%2 == 0):
            odd_string += s[i]
        elif (i%2 != 0):
            even_string += s[i]
        elif i == 0 :
            even_string += s[i]
    return f' {odd_string} {even_string}'

t = int(input())
for i in range(0, t):
    string = input()
    print(stringsplit(string))