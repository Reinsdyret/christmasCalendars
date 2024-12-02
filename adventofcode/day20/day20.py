
def insert(l, el, i):
    newList = l[:i]
    # print(newList)
    newList.append(el)
    newList.extend(l[i:])
    return newList


def shiftElem(elemList, elem):
    elemIndex = elemList.index(elem)
    newIndex = (elemIndex + elem)
    if (newIndex >= len(elemList)):
        newIndex = (newIndex % len(elemList)) + 1
    if (newIndex == 0):
        newIndex -= 1
    # print(f"shifting element {elem} from {elemIndex} to {newIndex}")
    if (newIndex == -1):
        # print(f"{elem} lands at -1")
        newIndex = len(elemList)
    # print(f"{newIndex = }")
    elemList.pop(elemIndex)
    return insert(elemList, elem, newIndex)


def indexAt(l, i):
    return l[i % len(l)]


lines = []

with open("day20Input.txt", 'r') as f:
    lines = f.readlines()

numbers = [int(a) for a in lines]
numbersCopy = [a for a in numbers]

if (len(numbers) < len(set(numbers))):
    print("There are duplicates")

for num in numbers:
    # print(numbersCopy)
    numbersCopy = shiftElem(numbersCopy, num)

zeroIndex = numbersCopy.index(0)
# print(numbersCopy)
print(zeroIndex)

print(f"{indexAt(numbersCopy, zeroIndex + 1000) + indexAt(numbersCopy, zeroIndex + 2000) + indexAt(numbersCopy, zeroIndex + 3000) = }")

