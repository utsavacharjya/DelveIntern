wor = input("Enter passwords (separate by commas):")
passlst = wor.split(",")
fin  = []
upcnt = 0
lowcnt = 0
numcnt = 0
schar = "$#@"
scnt = 0
for pss in passlst:
    if len(pss) < 6 or len(pss) > 12:
        continue
    for ch in pss:
        if ch.isupper():
            upcnt += 1
            continue
        elif ch.islower():
            lowcnt += 1
            continue
        elif ch.isnumeric():
            numcnt += 1
            continue
        elif ch in schar:
            scnt += 1
            continue
    if upcnt > 0 and lowcnt > 0 and numcnt > 0 and scnt > 0:
        fin.append(pss)
        upcnt, lowcnt, numcnt, scnt = 0, 0, 0, 0

print(*fin, sep = ",")