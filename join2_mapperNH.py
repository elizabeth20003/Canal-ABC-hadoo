#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line    = line.strip()
    key_value = line.split("\t")
    key     = key_value[0]
    value   = key_value[1]
    
    if value.isdigit():
        print('{0}\t{1}'.format(key, value))
    elif value=='ABC':
        value_2 = 0
        print('{0}\t{1}\t{2}'.format(key, value, value_2))

 