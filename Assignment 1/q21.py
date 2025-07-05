mnum = int(input("Enter number: "))
copy1 = mnum
dig = 0
ams = 0

while copy1 != 0:
    copy1 //= 10
    dig += 1

copy2 = mnum
while copy2 != 0:
    snum = copy2%10
    ams += snum ** dig
    copy2 //= 10

if ams == mnum:
    print("{0} is an Armstrong Number".format(mnum))
else:
    print("{0} is not an Armstrong Number".format(mnum))