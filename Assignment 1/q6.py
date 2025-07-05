wor = input("Enter sentence:")
upcnt = 0
lowcnt = 0
for ch in wor:
    if ch.isupper():
        upcnt += 1
    elif ch.islower():
        lowcnt += 1

print("UPPER CASE: {0} \nLOWER CASE: {1}".format(upcnt, lowcnt))