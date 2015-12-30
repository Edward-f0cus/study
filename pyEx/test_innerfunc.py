#!/usr/bin/env python

def Foo():
    print "this is Foo func"

def func(arg1, arg2=Foo()):
    print "this is func"
    def inner_func(arg3=arg2):
        print "this is inner func"
        return arg1, arg3
    arg1 = arg2 = 0
    return inner_func

if __name__  == '__main__':
    func('haha')

