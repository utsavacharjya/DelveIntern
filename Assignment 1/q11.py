par = input("Enter string: ")
par = par.casefold()
cnt = 0
ch = ""
fin = []
i = 0
while i < len(par) - 1:
    ch = par[i]
    cnt += 1
    for j in range(i + 1, len(par)):
        if par[j] == ch:
            cnt += 1
        else:
            break
    fin.append(ch)
    fin.append(str(cnt))
    i = j
    ch = ""
    cnt = 0

print(*fin, sep = "")