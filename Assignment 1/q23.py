mnum = int(input("Enter number: "))
sum = 0
divls = []
for i in range(1, mnum//2 + 1):
    if mnum % i == 0:
        divls.append(i)

for val in divls:
    sum += val

if sum == mnum:
    print("Perfect Number")
else:
    print("Not Perfect Number")