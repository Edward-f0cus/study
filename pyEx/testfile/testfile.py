#!/usr/bin/python

with open('test.txt') as f:
    for line in f.xreadlines():
        print line,
