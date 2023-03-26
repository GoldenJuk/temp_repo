
# Модуль сжатия 
import os  
   
def compress(input_file, output_file):  
    count = 1 
    current = None 
    output = "" 
    for line in open(input_file, 'r'):  
        for char in line:  
            if char != current:  
                if current is not None:  
                    output += current + str(count)  
                current = char  
                count = 1 
            else:  
                count += 1 
    else:  
        output += current + str(count)  
 
    with open(output_file, 'w') as f:  
        f.write(output)  
 
# Модуль восстановления 
import os  
   
def decompress(input_file, output_file):  
    count = 0 
    current = None 
    output = "" 
    for line in open(input_file, 'r'):  
        for char in line:  
            try:  
                count = int(char) 
                if current is not None:  
                    output += current * count 
            except ValueError: 
                current = char  
    else:  
        output += current * count 
 
    with open(output_file, 'w') as f:  
        f.write(output)
