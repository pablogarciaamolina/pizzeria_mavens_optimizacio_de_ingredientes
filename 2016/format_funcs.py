'''
Functions for formatting different fields
'''

import re
import pandas as pd

PIZZA_FORMAT_RELATIONS = {'3': 'e', '@': 'a', '0': 'o', ' ': '_', '-': '_'}
QUANTITY_FORMAT_RELATIONS = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def format_int(field: str) -> str:
    '''
    Formateo:
    - Comprobar que es entero
    '''
    
    try:
        int(field)
    except Exception:
        field = ''
    return field

def format_quantity(field: str) -> str:
    try:
        field = str(abs(int(field)))
    except Exception:
        field = field.lower()
        field = QUANTITY_FORMAT_RELATIONS[field]
    return field

def format_pizza_id(field: str) -> str:
    '''
    Formateo:
    - 3 -> e
    - @ -> a
    - 0 -> o
    - [ -] -> _
    '''
    for r in PIZZA_FORMAT_RELATIONS:
        field = re.sub(r, PIZZA_FORMAT_RELATIONS[r], field)
    return field

def format_date(field: str) -> str:
    
    try:
        date = str(pd.to_datetime(field))
        date_list = date.split(sep=' ')[0].split(sep='-')
        date = date_list[2] + '/' + date_list[1] + '/' + date_list[0]
    except Exception:
        date = ''
    
    return date

def format_time(field: str) -> str:
    return field + ' '

# if __name__ == '__main__': 