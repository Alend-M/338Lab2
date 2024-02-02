import timeit
import matplotlib.pyplot as plt 

def func1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func1(n-1) + func1(n-2)
#1.1: This code is an implementation of the fibonacci sequence using recursion.
    
#1.2:Yes, this is a example of divide and conquere because the code is broken 
#    down to lesser and lesser complex functions, where their results are added up. 

#1.3: The time complexity of the algorithm is O(n^2)
    
#1.4: 
def func2(n, memo):  #Throws in a dictionary of n and its results
    if n in memo:
        return memo[n]  #check if n's value is in memo
    if n == 0 or n == 1:
        return n
    else:
        memo[n] = func2(n-1, memo) + func2(n-2, memo)     #save results into memo under the n key
        return memo[n], memo  #return resaults 
    
#1.5    Average time complexity O(n^2). Best case time complexity O(1)

#1.6
memo = {}
func1Array = []
func2Array = []
array = list(range(35))

for x in range(35):
    func1Time = timeit.timeit(lambda:func1(x), number=1)
    func1Array.append(func1Time)
    func2Time = timeit.timeit(lambda:func2(x, memo), number=1)
    func2Array.append(func2Time)
print(len(array), "//" , len(func1Array))

print(f"Function 1 time: {func1Time:.8f}\nFunction 2 time: {func2Time:.8f}")
plt.plot(array, func1Array, label = "Function 1")
plt.xlabel('Input (n)')
plt.ylabel('Execution Time (seconds)')
plt.savefig('ex1.6.1.jpg')
plt.plot(array, func2Array, label = "Function 2")
plt.xlabel('Input (n)')
plt.ylabel('Execution Time (seconds)')
plt.savefig('ex1.6.2.jpg')
