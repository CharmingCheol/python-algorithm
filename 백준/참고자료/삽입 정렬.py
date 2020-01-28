arr2 = [1, 5, 7, 3, 2, 5, 8, 9, 3, 9, 6, 4, 4, 2, 7]
for i in range(len(arr2)):
    index = i
    while index > 0 and arr2[index-1] > arr2[index]:
        arr2[index-1], arr2[index] = arr2[index], arr2[index-1]
        index -= 1
print(arr2)

"""
import random


def insertion_sort(collection):
    for index in range(1, len(collection)):
        while 0 < index and collection[index] < collection[index - 1]:
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            index -= 1
    return collection


data_list = random.sample(range(100), 50)
print(data_list)
print(insertion_sort(data_list))
"""
