'''
Este algoritmo transformará los archivos de la variable UNFORMATTED a un formato válido, creando nuevos archivos con
el formato correcto.
Se basa en las especificaciones de formato de evaluation_readme.txt
'''

from io import TextIOWrapper
import time
import os
from format_funcs import *

UNFORMATTED = [['unformatted_order_details.csv',';'], ['unformatted_orders.csv',';']]
FORMAT_FUNC = {
    'order_details_id': format_int,
    'order_id': format_int,
    'pizza_id': format_pizza_id,
    'quantity': format_quantity,
    'date': format_date,
    'time': format_time
}

def mavens_formatting(file: TextIOWrapper, separator: str, new_file_name: str, new_sep=',') -> None:
    '''
    Creates the new and formatted file checking every field
    '''

    fields = file.readline()[:-1].split(sep=separator)
    n_fields = len(fields)
    header = ''
    for field in fields: header += field + new_sep
    
    print('...working...')

    with open(new_file_name, 'w') as new_file:
        new_file.write(header[:-1] + '\n')
        for line in file:
            new_line = ''
            writeable = True
            line_list = line[:-1].split(sep=separator)
            if '' in line_list: writeable = False
            if 'time' in fields: writeable = True
            
            if writeable:
                for i in range(n_fields):
                    formatted_str = FORMAT_FUNC[fields[i]](line_list[i])
                    new_line += formatted_str + new_sep
                    if formatted_str == '': writeable = False
                if writeable: new_file.write(new_line[:-1] + '\n')
    
def format_csv(name: str, sep: str) -> None:

    print(f'·Formatting {name}')
    try:
        start = time.perf_counter()
        file = open(name, 'r')
        mavens_formatting(file, separator=sep, new_file_name=name.replace('unformatted_', ''))
        file.close()
        end = time.perf_counter()
        print('<DONE>', f'({end-start} seconds)')
    except Exception as error: print('<UNABLE>', f'({error})')
    

if __name__ == '__main__':
    
    for element in UNFORMATTED: format_csv(element[0], element[1])