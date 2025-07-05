par = input("Enter string: ")
par = par.casefold()
sum = 0
temp = []
fin = []
for i in range(len(par)):
    if par[i].isalpha():
        for j in range(i + 1, len(par)):
            if par[j].isalpha():
                sum = 0
                for num in par[i+1:j]:
                    if num.isnumeric():
                        sum += int(num)
                if sum == 9:
                    temp.append(par[i])
                    temp.append(par[j])
                    fin.append(temp)
                    temp = []
                elif sum > 9:
                    sum = 0
                    break
                else:
                    sum = 0
                    temp = []

for val in fin:
    print(*val, sep = ",")