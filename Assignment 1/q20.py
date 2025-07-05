hpat = {"Sugar level": 15, "Blood pressure": 32, "Heartbeat rate": 71, "weight": 65, "fat percentage": 10}
inpat = {}
diff = {}
for keys in hpat:
    inp = int(input("Enter your {0}: ".format(keys)))
    inpat[keys] = inp
    diff[keys] = hpat[keys] - inpat[keys]

for keys in diff:
    if diff[keys] > 0:
        print("Your {0} is {1} less than the ideal value".format(keys.casefold(), diff[keys]))
    elif diff[keys] < 0:
        print("Your {0} is {1} more than the ideal value".format(keys.casefold(), abs(diff[keys])))
    else:
        print("Your {0} is ideal".format(keys.casefold()))