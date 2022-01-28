L = [1,3,5-9,13]

result = []
for i in L:
    if str(i).isnumeric():
        result.append(i)
    elif not str(i).isnumeric():
        print(str(i).split(('-')))
        start,stop = map(int,str(i).split('-'))
        for j in range(start,stop+1):
            result.append(j)

print(result)

