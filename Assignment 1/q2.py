wor = input("Enter words (separate by comma):")
worls = wor.split(",")
worls.sort()
print(*worls, sep = ",")