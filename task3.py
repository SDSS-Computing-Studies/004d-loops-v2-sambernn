numList = (5, 7, 11, 15, 27, 35)

for i in numList:
    numList = i/5
    x = int(numList)
    if x == numList:
        print(i)