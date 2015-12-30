#!/usr/bin/env python


def outer():
    para = 1
    print 'this is outer func'

    def inner():
        print 'this is inner func'
        print 'outer para in inner is %s' % para
        return para
    return inner()

print outer()
print para
