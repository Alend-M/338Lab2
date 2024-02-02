#   • In this exercise, you will implement basic search algorithms and attempts to
#   confirm theoretical complexity findings with empirical measures
#   1. Implement linear search and binary search [0.5 pts]
#   2. Measure the performance of each on sorted vectors of 1000, 2000, 4000,
#   8000, 16000, 32000 elements . In each case, you must do the following for
#   1000 times, and compute the average [0.5 pts]:
#       a. Pick a random element in the vector
#       b. Measure the time it takes to find the element using timeit, using 100
#       iterations (number=100)

def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1


def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1