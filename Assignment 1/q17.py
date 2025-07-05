wor = input("Enter email address:")
schar = "._@"
cnt = 0
valid = True
for ch in wor:
    if ch in "@":
        cnt += 1

if cnt != 1:
    valid = False

for ch in wor:
    if ch.islower():
        continue
    elif ch.isnumeric():
        continue
    elif ch in schar:
        continue
    else:
        valid = False
        break

if valid:
    print("Valid ID")
else:
    print("Invalid ID")