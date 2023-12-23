A = [0] * 30000
s = input()
C, D = [], []
n = 0
cnt = 0
flag = False
if '[' in s:
    for i in range(len(s)):
        if s[i] == '[':
            C.append(i)
    for i in C:
        k = i
        n = 0
        while n != -1:
            k += 1
            if s[k] == '[':
                n += 1
            elif s[k] == ']':
                n -= 1
        D.append([i, k])
i, j = 0, 0
while j != len(s):
    if s[j] == '+':
        if A[i] == 255:
            A[i] = 0
        else:
            A[i] += 1
    elif s[j] == '[':
        if A[i] == 0:
            for k in D:
                if k[0] == j:
                    j = k[1]
                    break
    elif s[j] == ']':
        for p in D:
            if p[1] == j:
                j = p[0] - 1
                break
    elif s[j] == '-':
        if A[i] == 0:
            A[i] = 255
        else:
            A[i] -= 1
    elif s[j] == '>':
        if i < 30000:
            i += 1
        else:
            i -= 30000
    elif s[j] == '<':
        if i == -30000:
            i = 29999
        else:
            i -= 1
    else:
        print(A[i])
    j += 1


