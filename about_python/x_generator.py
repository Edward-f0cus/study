#!/usr/bin/env python
import sys
import pdb

pdb.set_trace()


def fibo_gen(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibo_iter(n):
    a = b = 1
    l = []
    for i in range(n):
        l.append(a)
        a, b = b, a + b
    return l


method_used = sys.argv[1]
method_used = 'fibo_iter(3)' if method_used == 'iter' else 'fibo_gen(3)'
# for item in eval(method_used):
for item in fibo_gen(3):
    print item
