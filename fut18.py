#! /usr/bin/env python3
# -*- coding: utf-8; -*-
import sys
import re

def write_specials(file):
    for player_id in specials_set:
        out = '&quot;'+player_id+'&quot;:0,'
        file.write(out)

if(len(sys.argv) != 3):
    print("ERROR: Se necesitan dos argumentos")
    print("Uso:",sys.argv[0],"archivo_fut18 N")
    print("-El nombre del archivo debe ser algo parecido a 'com.pacybits.fut18draft_preferences.xml'")
    print("-N especifica el numero de veces que apareceran repetidos todos los jugadores")
    sys.exit(1)

#check if is integer
try:
    N = int(sys.argv[2])
except ValueError:
    print ("ERROR:'",sys.argv[2],"' no es un numero valido")
    sys.exit(1)

#recover str
N = sys.argv[2]

try:
    input_f = open(sys.argv[1],'r')
except FileNotFoundError:
    print ("ERROR: El archivo'",sys.argv[1]," 'no existe")
    sys.exit(1)

out_f  = open('HACKED_'+sys.argv[1],'w')

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

#special cards => just 0
#id -2,-3 Pacybits SBC
#-4 bechkam pacybits icon
#-5 a -11 sbc premium
#-12 xabi alonso pacybits icon
#-13 umtiti
#-14 -15 terry and huntelaar

id_set=[]
specials_set=['-2','-3','-4','-5','-6','-7','-8','-9','-10','-11','-12','-13','-14','-15']

#fill id_set with all players
for line in input_f:
    id_set += set(re.findall(regex_id,line))

i = 0
id_set = set(id_set)

#read file again and write
input_f.seek(0)
for line in input_f:
    if regex_players_line.match(line):
        #write to player db
        out_f.write('<string name="bXlfaWRz">{')
        write_specials(out_f)
        for player_id in id_set:
            i+=1
            if(i == len(id_set)):#last player, dont write comma
                out = '&quot;'+player_id+'&quot;:'+N
            else:
                out = '&quot;'+player_id+'&quot;:'+N+','
            out_f.write(out)

        out_f.write('}</string>\n')

    else:
        out_f.write(line)

out_f.close()
input_f.close()
