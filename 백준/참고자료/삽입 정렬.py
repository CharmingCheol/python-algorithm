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
