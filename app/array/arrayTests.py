from arrayDefs import *

array = [10, 23, 14, 19, 5, 3, 12]
print('your array is {}'.format(array))

average_val = average_value(array)
print('average value is {}'.format(average_val))

dispersion = dispersion(array, average_val)
print('dispersion is {}'.format(dispersion))

deviation = deviation(dispersion)
print('deviation is {}'. format(deviation))
