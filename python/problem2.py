###
#problem2.py
###
''' Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''
from math import sqrt

def fib(n):
    a,b = 0,1
    fib_nums = []
    while b < n:
        a,b = b, a+b
        if b % 2 == 0:
            fib_nums.append(b)
    return sum(fib_nums)

'''
even_fibs = []
for index, fib_num in enumerate(fib()):
    if fib_num % 2 == 0:
        even_fibs.append(fib_num)
    #print('{i:3}: {f:3}'.format(i=index, f=fib_num))
    if index == 4000000:
        break
'''
print fib(4000000)
#print sum(even_fibs)

   

