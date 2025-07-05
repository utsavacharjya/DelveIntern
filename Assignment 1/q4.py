fin = []
for i in range(1000, 3001):
    temp = i
    while i > 0:
        div = i % 10
        if div % 2 == 0:
            if 0 < i < 10:
                fin.append(temp)
                i = int(i / 10)
            else:
                i = int(i / 10)
        else:
            break

print(*fin, sep = ",")