def average_value(array):
    average = 0.0
    for i in range(len(array)):
        average += array[i]
    return average/len(array)


def dispersion(array, average_vaue):
    sqr_diff = 0.0
    for i in range(len(array)):
        sqr_diff += pow((float(array[i])-average_vaue), 2)
    return sqr_diff/len(array)


def deviation(dispersion):
    deviation = pow(dispersion, 0.5)
    return deviation
