#a
row = int(input("Enter rows: "))
num = 1

for i in range(1, row + 1):
    for j in range(i):
        if j == i - 1:
            print(num)
        else:
            print(num, end = "*")
        num += 1
    print()

#b
row = int(input("Enter rows: "))

for i in range(1, row + 1):
    print(" " * (row - i), end='')
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(row - 1, 0, -1):
    print(" " * (row - i), end='')
    for j in range(i):
        print("*", end=" ")
    print()

#c
row = int(input("Enter rows: "))
num = 1

for i in range(1, row + 1):
    for j in range(i):
        print(num, end="")
        num += 1
        if j != i - 1:
            print(" * ", end='')
    print()

num -= row

for i in range(row - 1, 0, -1):
    num -= i
    temp = num
    for j in range(i):
        print(temp, end="")
        temp += 1
        if j != i - 1:
            print(" * ", end="")
    print()

#e
row = int(input("Enter rows (only odd): "))

for i in range(row):
    for j in range(row):
        if i == 0 or i == row - 1:
            print(1, end=" ")
        elif j == row // 2:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()