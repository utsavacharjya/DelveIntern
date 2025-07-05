inp = "y"
translst = []
amount = 0
while inp == "y":
    trans = input("Enter mode (W or D) and amount: ")
    cont = input("Do you want to continue (y or n): ")
    inp = cont.casefold()
    temp = trans.split()
    translst.append(temp)

for val in translst:
    if val[0].casefold() == "w":
        if amount < int(val[1]):
            print("Not enough balance")
        else:
            amount -= int(val[1])
    elif val[0].casefold() == "d":
        amount += int(val[1])
    else:
        print("Invalid Input")

print("Total Balance: {0}".format(amount))