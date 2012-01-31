#encoding: utf-8

import sys

filename = sys.argv[1]
with open(filename) as f:
    print '='*60
    for i, line in enumerate(f):
        print format(i,'3'), line.rstrip()
    print '='*60
