rocol = input("Enter row and col (separate by comma): ")
lst = rocol.split(",")
row = int(lst[0])
col = int(lst[1])
temp = []
matr = []
for i in range(row):
    for j in range(col):
        temp.append(i*j)
    matr.append(temp)
    temp = []

print(matr)