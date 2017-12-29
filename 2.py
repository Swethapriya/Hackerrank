#!/bin/python

import sys

def fibs(n):
    sol = 0
    i = 1
    while(True):
        if(fib(i)>n):
            break
        else:
            num = fib(i)
            if(num%2 ==0):
                sol += num
        i += 1
    print sol
#return nth fib
def fib(n):
    if(n > len(res)):
        res.append(fib(n-1) + fib(n-2))
    return res[n-1]

res = [1,2]
t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    fibs(n)

