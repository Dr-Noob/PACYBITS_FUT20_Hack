#! /usr/bin/env python3

import sys
import re
import base64

if(len(sys.argv) != 2):
    print("ERROR: Need one arg")
    print("Use:",sys.argv[0],"file")
    sys.exit(1)

try:
    input_f = open(sys.argv[1],'r')
except FileNotFoundError:
    print ("ERROR: File '",sys.argv[1],"' does not exist")
    sys.exit(1)

regex_item = re.compile(r'\s*<string\s+name="([^"]+)">([^<]+)</string>')

sys.stdout.write("<?xml version='1.0' encoding='utf-8' standalone='yes' ?>\n")
sys.stdout.write("<map>\n")

for line in input_f:
    if regex_item.match(line):
        m = re.search(regex_item, line)
        sys.stdout.write("    <string name=\"")
        sys.stdout.write(base64.b64encode(bytes(m.group(1), 'utf-8')).decode("utf-8"))
        sys.stdout.write("\">")
        sys.stdout.write(base64.b64encode(bytes(m.group(2), 'utf-8')).decode("utf-8"))
        sys.stdout.write("</string>\n")

sys.stdout.write("</map>\n")
