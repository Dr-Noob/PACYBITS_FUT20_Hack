#! /usr/bin/env python3
# -*- coding: utf-8; -*-
import sys
import re

if(len(sys.argv) != 3):
    print("ERROR: Se necesitan dos argumentos")
    print("Uso:",sys.argv[0],"archivo_fut18 N")
    print("-El nombre del archivo debe ser algo parecido a 'com.pacybits.fut18draft_preferences.xml'")
    print("-N especifica el numero de veces que apareceran repetidos todos los jugadores")
    sys.exit(1)

try:
    f = open(sys.argv[1],'r')
except FileNotFoundError:
    print ("ERROR: El archivo",sys.argv[1],"no existe")
    sys.exit(1)

n  = open('HACKED_com.pacybits.fut18draft_preferences.xml','w')

regex_player = r'&quot;(\d+)&quot;:(\d+),'
regex_id = r'id&quot;:&quot;(\d+)'

regex_players_line = re.compile(r'^    <string name="bXlfaWRz">.*')
regex_id_line_1 = re.compile(r'^    <string name="YWxsX3BsYXllcnM=">.*') #icn,gold,silver,some ifs and some otw
regex_id_line_2 = re.compile(r'^    <string name="dXBkYXRlXzY=">.*') #halloween and kane award winner
regex_id_line_3 = re.compile(r'^    <string name="dXBkYXRlXzk=">.*') #fut champs gold
regex_id_line_4 = re.compile(r'^    <string name="b3R3X3BsYXllcnM=">.*') #salah and sigurdson hero
regex_id_line_5 = re.compile(r'^    <string name="dXBkYXRlXzg=">.*') #?? new ifs
regex_id_line_6 = re.compile(r'^    <string name="bGF0ZXN0X3VwZGF0ZV9wbGF5ZXJz=">.*') #new ifs
regex_id_line_7 = re.compile(r'^    <string name="dXBkYXRlXzc=">.*') #giroud award winner,some ifs
regex_id_line_8 = re.compile(r'^    <string name="dXBkYXRlXzQ=">.*')
regex_id_line_9 = re.compile(r'^    <string name="dXBkYXRlXzU=">.*')
regex_id_line_10 = re.compile(r'^    <string name="dXBkYXRlXzM=">.*')
regex_id_line_11 = re.compile(r'^    <string name="bGF0ZXN0X3RvdHdfcGxheWVycw=">.*')
regex_id_line_12 = re.compile(r'^    <string name="c2JjX3BsYXllcnM=">.*')
regex_id_line_13 = re.compile(r'^    <string name="c2F2ZWRfZHJhZnRz=">.*')
regex_id_line_14 = re.compile(r'^    <string name="c2F2ZWRfc3F1YWRz=">.*')

id_set=[]

#fill id_list with all players
for line in f:
    id_set += set(re.findall(regex_id,line))
    '''
    if regex_id_line_1.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_2.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_3.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_4.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_5.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_6.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_7.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_8.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_9.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_10.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_11.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_12.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_13.match(line):
        id_set += set(re.findall(regex_id,line))
    elif regex_id_line_14.match(line):
        id_set += set(re.findall(regex_id,line))
    '''
f.seek(0)
i = 0
id_set = set(id_set)
#read file again and write
for line in f:
    if regex_players_line.match(line):
        '''
        out = re.sub(regex_player,r'&quot;\1&quot;:10,',line)
        out = out[:-11] #delete end of string to introduce new players
        n.write(out)
        n.write(',')
        '''
        n.write('<string name="bXlfaWRz">{')
        for player_id in id_set:
            i+=1
            if(i == len(id_set)):
                out = '&quot;'+player_id+'&quot;:10'
            else:
                out = '&quot;'+player_id+'&quot;:10,'
            n.write(out)

        n.write('}</string>\n')

    else:
        n.write(line)

n.close()
f.close()
