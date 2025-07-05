import math

inp = "y"
movlst = []
amount = 0
fin = []
while inp == "y":
    rob = input("Enter direction (up, down, left, right) and dist: ")
    cont = input("Do you want to continue (y or n): ")
    inp = cont.casefold()
    temp = rob.split()
    movlst.append(temp)

vertcnt = 0
horicnt = 0

for val in movlst:
    if val[0].casefold() == "up":
        vertcnt += int(val[1])
    elif val[0].casefold() == "down":
        vertcnt -= int(val[1])
    elif val[0].casefold() == "left":
        horicnt -= int(val[1])
    elif val[0].casefold() == "right":
        horicnt += int(val[1])
    else:
        print("Invalid Input")

sumsq = abs(vertcnt)**2 + abs(horicnt)**2
dist = math.sqrt(sumsq)
findist = round(dist)
print(findist)