mnum = int(input("Enter number: "))
copy = mnum
bin = ""
while copy != 0:
    temp = copy % 2
    bin += str(temp)
    copy //= 2

fin = bin[-1::-1]
print(int(fin))