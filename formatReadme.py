#!/usr/bin/env python

import sys

out_line = []
out_file = None
out_line_char_num = 0

def write_line():
    global out_line
    global out_file
    global out_line_char_num

    out_file.write( ''.join(out_line) )
    out_file.write("\n")
    out_line = []
    out_line_char_num = 0

def fix_file(file_name):
    global out_line
    global out_file
    global out_line_char_num

    with open(file_name, "r") as f:
        icontent = f.readlines()
    
    out_file = open('new-README', "w")
    out_line = []
    out_line_char_num = 0

    for rline in icontent:
        line = rline.strip()
        if len(line) < 2:
            write_line()
            out_file.write("\n")
            continue

        for word in line.split():
           if (len(out_line) + out_line_char_num) > 75:
               write_line()
           else:
               out_line_char_num += len(word)
               out_line.append(word)
               out_line.append(' ')

    write_line()

if __name__ == "__main__":
    fix_file(sys.argv[1])
