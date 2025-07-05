import math

n = int(input("Enter bus stops: "))
m = int(input("Enter mandatory stops: "))

if m > (n + 1) // 2:
    print("No way to avoid consecutive stops")
else:
    num = math.comb(n - m + 1, m)
    print("There are {0} ways to avoid consecutive stops".format(num))