wor = input("Enter words (separate by whitespace):")
worls = wor.split(" ")
worls.sort()
fin = []
for val in worls:
    if val not in fin:
        fin.append(val)
print(*fin, sep = " ")