'''
1. What is a profiler, and what does it do? [0.25 pts]
        A profiler measures the performance of a program. This includes "how often
        and for how long various parts of the program are executed". 
        https://docs.python.org/3/library/profile.html

2. How does profiling differ from benchmarking? [0.25 pts]
        Profiling means measuring the internal behaviours of the program
        (Where the program spends the most time or consumes the most resources).
        Benchmarking measures the system's overall performance, and how it performs
        with diffferent data.
        https://www.oreilly.com/library/view/high-performance-mysql/9780596101718/ch02.html

3. Use a profiler to measure execution time of the program (skip function
definitions) [0.25 pt]

        Output: 
        test_function:

        69 function calls (24 primitive calls) in 0.000 seconds
        Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    55/10    0.000    0.000    0.000    0.000 ex3.py:24(sub_function)
        1    0.000    0.000    0.000    0.000 ex3.py:31(test_function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

        third_function:

        5 function calls in 53.455 seconds
        Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    5.434    5.434   53.455   53.455 <string>:1(<module>)
        1    0.000    0.000   48.021   48.021 ex3.py:37(third_function)
        1   48.020   48.020   48.020   48.020 ex3.py:39(<listcomp>)
        1    0.000    0.000   53.455   53.455 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

4. Discuss a sample output. Where does execution time go? [0.25 pts]
        The total time spent in the given funtion (per row), excluding time made in calls to sub funtions 
        is under the [tottime] column. 
        The cumulative time spent in the function (per row), including sub funtions, is in the [cumtime] column.
        To find the execution time of the entire program, including recursive calls, 
        you should (probably) sum the [cumtime] column.'''


import timeit
import cProfile
import re

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


cProfile.run("test_function()")
cProfile.run("third_function()")



