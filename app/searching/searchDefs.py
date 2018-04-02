def linear_search(array, target):
    result = 'not found'
    for i in range(len(array)):
        if target == array[i]:
            result = i
    return result


def linear_list_search(list, target):
    result = 'not found'
    while list.next:
        if target == list.data:
            result = list
            return result
        list = list.next
    return result


def binary_search(array, target):
    result = 'not found'
    arr_min = 0
    arr_max = len(array) - 1
    while arr_min <= arr_max:
        arr_mid = int((arr_max + arr_min) / 2)
        if target < array[arr_mid]:
            arr_max = arr_mid - 1
        else:
            if target > array[arr_mid]:
                arr_min = arr_mid + 1
            else:
                return arr_mid
    return result


def interpolation_search(array, target):
    result = 'not found'
    arr_min = 0
    arr_max = len(array) - 1
    while arr_min <= arr_max:
        arr_mid = int(arr_min + (arr_max - arr_min) * (target - array[arr_min]) / (array[arr_max] - array[arr_min]))
        if array[arr_mid] == target:
            return arr_mid
    return result
