#!/usr/bin/env python
def a(x, y):
    return x + y


def b():
    for i in range(12):
        yield i

#c = (i for i in range(12))
c = b()

#for j in [1, 122, 1, 4, 5, 2, 1]:
#for j in [1, 255]:
    # c = (a(i, j) for i in c)
    #x = x + 1
    #if x == 2:
    #   for n in c:
    #       print n
#    def __gen(exp):
#        for y in exp:
#            yield a(y, j)
#    c = __gen(c)

j = 1
#c = (a(i, j) for i in c)
def __gen(exp):
    for i in exp:
        yield a(i, j)
c = __gen(c)
j = 22
#c = (a(i, j) for i in c)
def __gen1(exp):
    for i in exp:
        yield a(i, j)
c = __gen1(c)
j = 33
def __gen2(exp):
    for i in exp:
        yield a(i, j)
c = __gen2(c)
#c = (a(i, j) for i in c)
j = 8
#c = (a(i, j) for i in c)
def __gen3(exp):
    for i in exp:
        yield a(i, j)
c = __gen3(c)

# print list(c)
for m in c:
    print m
