#!/bin/bash/python

import os
fileName = raw_input('Please enter your file name: ')
#with open(fileName, 'w') as f:
f = open(fileName, 'w')
while True:
    content = raw_input('please enter your line content: ')
    if content != '.':
        f.write(content + os.linesep)
    else:
        break
f.close()
