from sortingDefs import *
import time
import random

array = []
array_len = 20

randomize_array(array, array_len)

print('\n randomized {} items in array: \n {}'.format(array_len, array))

tic = time.time()
insert_sort(array)
toc = time.time()
print('\n sorted by insert_sort: \n {} \n done in {}'.format(array, toc-tic))

random.shuffle(array)
print('\n shuffled: \n {}'.format(array))

tic = time.time()
picking_sort(array)
toc = time.time()
print('\n sorted by picking_sort: \n {} \n done in {}'.format(array, toc-tic))

random.shuffle(array)
print('\n shuffled: \n {}'.format(array))

tic = time.time()
bubble_sort(array)
toc = time.time()
print('\n sorted by bubble_sort: \n {} \n done in {}'.format(array, toc-tic))

clear_array(array)
print('\n array cleared:')
print(array)
