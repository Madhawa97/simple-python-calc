from math import sqrt 

def add(n, m):
    return n+m

def sub(n, m):
    return n-m

def mul(n, m):
    return n*m

def div(n, m):
    x = float(n)/float(m)
    return x

def fac(n):
    if n < 0:
        return "Wrong Input"
    elif n == 1 or n == 0:
        return 1
    else:
        return n*fac(n-1)

def root(n):
    return sqrt(n)

def squared(n):
    return n*n


