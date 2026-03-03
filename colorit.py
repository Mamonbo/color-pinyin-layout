import sys
import re

if len(sys.argv) <= 1:
    exit(0)
else:
    #print(sys.argv[1])
    filename=sys.argv[1]

color_map=dict([])
color_map['a']=(255,0,0)
color_map['o']=(0,0,255)
color_map['e']=(255,120,30)
color_map['u']=(240,56,230)
color_map['i']=(32,192,158)
color_map['v']=(32,192,158) # for "ü"

color_map['n']=(74,66,14)

with open(filename) as f:
    for line in f:
        if '<text' in line and 'rgb(155,155,155)' in line:
            # gray sub-text
            mch_obj=re.search('>([a-z]+)<',line)
            #print(mch_obj.group(1))
            if mch_obj==None:
                print(line,end="")
                continue
            
            cont=mch_obj.group(1)
            mojir=line.replace('(155,155,155)',str(color_map[cont[0]]))
            print(mojir,end="")
            if 'ng' in cont:
                mojir=line.replace('(155,155,155)',str(color_map['n']))
                mojir2=re.sub('>([a-z]+)<','>ng<',mojir)
                print(mojir2,end="")
            elif 'n' in cont:
                mojir=line.replace('(155,155,155)',str(color_map['n']))
                mojir2=re.sub('>([a-z]+)<','>n<',mojir)
                print(mojir2,end="")
        else:
            print(line,end="")

print('')
