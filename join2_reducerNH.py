#!/usr/bin/env python3

import sys

show_name_list = []
show_viewer_tuple_list = []

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def remove_nonABCshows(values):
    output = []
    for value in values:
        if value[0] in show_name_list:
            output.append(value)
    return output

for input_line in sys.stdin:
    input_line = input_line.strip()

this_key, values = input_line.split("\t", 1)

chanelname_number = values.split("\t")
if chanelname_number[0]=='ABC':
    show_name_list.append(this_key)
else:
    tup = [this_key, values]
    show_viewer_tuple_list.append(tup)

show_name_list = remove_duplicates(show_name_list)

show_viewer_tuple_list = remove_nonABCshows(show_viewer_tuple_list)

show_viewer_tuple_list.append(("dummy_key", "0"))
pre_tup = show_viewer_tuple_list[0]
pre_key = pre_tup[0]
count = int(pre_tup[1])
for index in range(1, len(show_viewer_tuple_list)):
    curr_tup = show_viewer_tuple_list[index]
    key = curr_tup[0]
    value = curr_tup[1]
    if pre_key==key:
        count += int(value)
    else:
        print("{0}\t{1}".format(pre_key, count))
        pre_key = key
        count = 0
