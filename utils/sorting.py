# quick sort
from random import randint
def quickSort(lst):
    if len(lst) <= 1:
        return lst
    index = randint(0, len(lst) - 1)
    pivot = lst[index]
    lower, same, higher = [], [], []
    for elem in lst:
        if elem < pivot:
            lower.append(elem)
        elif elem == pivot:
            same.append(elem)
        else:
            higher.append(elem)

    return quickSort(lower) + same + quickSort(higher)

def mySearch(lst, condition):
    result = []
    for i in range(len(lst)):
        if condition(lst[i]):
            result.append(lst[i])
    return result

def mySort(lst, relation):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if not relation(lst[i], lst[j]):
                lst[i], lst[j] = lst[j], lst[i]