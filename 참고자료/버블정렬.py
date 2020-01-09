import random

def bubble_sort(data_list):
    for index in range(len(data_list) - 1):
        for index2 in range(len(data_list) - index - 1):
            print(index2)
            if data_list[index2] > data_list[index2 + 1]:
                data_list[index2], data_list[index2 + 1] = data_list[index2 + 1], data_list[index2]
    return data_list

data_list = random.sample(range(100), 50)
print(bubble_sort(data_list))