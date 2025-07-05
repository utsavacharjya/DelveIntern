valcurr = list(map(int, input("Enter valid currency denominations (separate by comma): ").split(",")))
mon = int(input("Enter the amount of money: "))

valcurr.sort(reverse=True)

for val in valcurr:
    if mon >= val:
        count = mon // val
        print(f"{val} - {count}")
        mon -= count * val
    if mon == 0:
        break