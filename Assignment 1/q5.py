wor = input("Enter sentence:")
alphacnt = 0
numcnt = 0
for ch in wor:
    if ch.isalpha():
        alphacnt += 1
    elif ch.isnumeric():
        numcnt += 1

print("LETTERS: {0} \nDIGITS: {1}".format(alphacnt, numcnt))