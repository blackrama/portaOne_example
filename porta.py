def MakeArray(fileName):
    intNumbers = []
    file = open(fileName,'r')
    numberArray = file.read().splitlines()
    file.close()
    for num in numberArray:
        intNumbers.append(int(num))
    return intNumbers

numbersArray = MakeArray('10m.txt')

maxNumber = max(numbersArray)
minNumber = min(numbersArray)
sortedArray = sorted(numbersArray)
lenSorted = len(sortedArray)
centerElement = int((lenSorted-1)/2)

print('maxNumber :',maxNumber)
print('minNumber :',minNumber)
print('mediana :',sortedArray[centerElement])
average = 0
for elem in sortedArray:
    average+=elem
print('average: ',average/lenSorted)


def LongestIncreasingList(a):
    lds, current = [], [a[0]]
    for val in a[1:]:
        if val > current[-1]:
            current.append(val)
        else:
            lds = current[:] if len(current) > len(lds) else lds
            current = [val]
    lds = current[:] if len(current) > len(lds) else lds
    return lds


print('Increasing: ',LongestIncreasingList(numbersArray))

def LongestDecreasingSublist(a):
    lds, current = [], [a[0]]
    for val in a[1:]:
        if val < current[-1]:
            current.append(val)
        else:
            lds = current[:] if len(current) > len(lds) else lds
            current = [val]
    lds = current[:] if len(current) > len(lds) else lds
    return lds
print('Descreasing: ',LongestDecreasingSublist(numbersArray))
