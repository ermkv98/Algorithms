from random import randint


def clear_array(array):
    for i in range(len(array)):
        array.pop()
    return array


def randomize_array(array, array_len):
    for i in range(array_len):
        x = randint(1, 100)
        array.append(x)
    return array


def insert_sort(array):
    for i in range(1, len(array)):
        buff = array[i]
        j = i - 1
        while j >= 0 and array[j] > buff:
            # move to right in one point
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = buff
    return array


def picking_sort(array):
    for i in range(len(array) - 1):
        minimal = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimal]:
                minimal = j
        array[i], array[minimal] = array[minimal], array[i]
    return array


def bubble_sort(array):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i+1], array[i] = array[i], array[i+1]
                not_sorted = True
    return array
