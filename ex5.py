#   • In this exercise, you will implement basic search algorithms and attempts to
#   confirm theoretical complexity findings with empirical measures
#   1. Implement linear search and binary search [0.5 pts] done
#   2. Measure the performance of each on sorted vectors of 1000, 2000, 4000,
#   8000, 16000, 32000 elements . In each case, you must do the following for
#   1000 times, and compute the average [0.5 pts]:
#       a. Pick a random element in the vector
#       b. Measure the time it takes to find the element using timeit, using 100
#       iterations (number=100)

import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return "not found"


def binary_search(arr, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:     
        return "not found"


array_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

for arr_size in array_sizes:
    arr= sorted(random.sample(range(arr_size), arr_size))
    find_this = random.choice(arr)

    #linear search's time
    linear_search_time = timeit.timeit("for _") #wait what

    #binary search's time