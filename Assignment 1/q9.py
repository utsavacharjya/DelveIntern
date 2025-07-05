inp = "y"
perlst = []
amount = 0
fin = []
while inp == "y":
    per = input("Enter name, age, score: ")
    cont = input("Do you want to continue (y or n): ")
    inp = cont.casefold()
    temp = per.split(",")
    perlst.append(temp)

perlst.sort()

for val in perlst:
    val[1] = int(val[1])
    val[2] = int(val[2])

for val in perlst:
    fin.append(tuple(val))

print(fin)