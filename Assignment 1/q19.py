rot = int(input("Enter rotation direction(1 - R-L; 2 - L-R): "))
mstr = input("Enter string: ").casefold()
tim = int(input("Number of times for rotation: "))
ans = ""
num = 1

if rot == 1:
    while tim > 0:
        ans = mstr[1:len(mstr)]
        ans += mstr[0]
        mstr = ans
        print("After rotation {0}: {1}".format(num, mstr))
        tim -= 1
        num += 1
elif rot == 2:
    while tim > 0:
        ans = mstr[len(mstr) - 1]
        ans += mstr[0:len(mstr) - 1]
        mstr = ans
        print("After rotation {0}: {1}".format(num, mstr))
        tim -= 1
        num += 1
else:
    print("Invalid input")