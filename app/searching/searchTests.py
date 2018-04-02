from searchDefs import *
from random import randint
import time


class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def init_array(array, array_len):
    for i in range(array_len):
        array.append(i)


def init_list(list, list_len):
    for i in range(list_len):
        list.next = Node(i)
        list = list.next


array = []
array_len = 1000000
init_array(array, array_len)

target = randint(0, array_len - 1)

print('\narray initialized with values from 0 to {}, target is {}'.format(array_len - 1, target))

tic = time.time()
position = linear_search(array, target)
toc = time.time()
print('\nLINEAR: target position {}, done in {}'.format(position, toc - tic))

list = Node('sentinel')
list_len = array_len
init_list(list, list_len)

print('\nlist initialized with values from 0 to {}, target is {}'.format(list_len - 1, target))

tic = time.time()
position = linear_list_search(list, target)
toc = time.time()
print('\nLINEAR_LIST: target node {}, done in {}'.format(position, toc - tic))

tic = time.time()
position = binary_search(array, target)
toc = time.time()
print('\nBINARY: target position {}, done int {}'.format(position, toc - tic))

tic = time.time()
position = interpolation_search(array, target)
toc = time.time()
print('\nINTERPOLATION: target position {}, done int {}'.format(position, toc - tic))
