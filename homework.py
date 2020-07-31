aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

aList = [1, 2, 3, 4, 5, 6, 7]
aList = [x * x for x in aList]
print(aList)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
resList = [x + y for x in list1 for y in list2]
print(resList)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)

    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
resList = list(filter(None, list1))
print(resList)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]

list1[2][1][2].extend(subList)
print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)
list1[index] = 200
print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]


def removeValue(sampleList, val):
    return [value for value in sampleList if value != val]


resList = removeValue(list1, 20)
print(resList)
