#! /usr/bin/env python

import re

f = open('test-sample.log')
lines = f.readlines()
f.close()

reg = re.compile("\] (\w.*)\ <=.*\ T=(.*)")

for line in lines:
    r = reg.search(line)
    if r:
        print "MSG ID =>", r.groups()[0], "Subject =>", r.groups()[1]
