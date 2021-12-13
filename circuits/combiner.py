import os

base = os.getcwd()

path_gcode = f"{base}\\test.nc"

print(path_gcode)
 
output = ""

position = 0

origins = ['G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', #1
           'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', #2
           'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', #3
           'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', #4
           'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', #5
           'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25', 'G92 X-17 Y-25'] #6
    

with open( path_gcode , 'r') as g:
    
    gcode = g.read()

    for i in range(len(origins)):
        output += "\n\n"
        output += origins[position]
        output += "\n\n"
        output += gcode
        position +=1

with open('res.nc', 'w') as f:
   f.write(output)