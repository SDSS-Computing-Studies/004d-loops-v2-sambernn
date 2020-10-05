numList = (25, 8, 10, 11, 33, 30, 51, 75, 63, 14, 20, 99)

for i in numList:
    numList = i/5
    x = int(numList)
    if x == numList:
        print(i)