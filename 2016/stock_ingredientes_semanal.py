'''
Pizzerias Maven
---------------
Obtaining optimized list of ingredients to buy weekly.
Based on year's 2016 data.

NOTE: Quantity values of the obtained .csv file with the optimized ingredients for each week represent the ratio of
units relative to the ingredient used in the making of every pizza. For example, if the ingredient "Tomatoes" described
in pizza_types.csv means n tomatoes per pizza, the the number of tomatoes needed is n*(ratio of units), if it means n
slices of tomato are needed then n*(ratio of units) slices of tomatoe are needed. QUANTITY DOES NOT HAVE UNITS,
IT DEPENDS ON THE INGREDIENT REFERENCED IN pizza_types.csv.
'''

import pandas as pd
from maven_classes import Pizza, Order
from format_csv_as_txt import format_csv
import os

os.system('cls')
format_csv('../maven_datasets/unformatted_order_details.csv', sep=';')
format_csv('../maven_datasets/unformatted_orders.csv', sep=';')
DF_ORDER_DETAILS = pd.read_csv('../maven_datasets/order_details.csv')
DF_ORDERS = pd.read_csv('../maven_datasets/orders.csv')
DF_PIZZA_TYPES = pd.read_csv('../maven_datasets/pizza_types.csv')
DF_PIZZAS = pd.read_csv('../maven_datasets/pizzas.csv')

SIZE_MULTIPLIER = {'S': 1, 'M': 2, 'L': 3, 'XL': 4, 'XXL': 5}
N_SIZES = len(SIZE_MULTIPLIER)

MONTH_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31, 12: 30}
N_YEARS = 1

def clear():
    os.system('cls')

#EXTRACT
def _get_pizzas_() -> list[Pizza]:
    
    pizzas = []
    # Extracting data from pizzas.csv
    for line in DF_PIZZAS.iloc():
        pizzas.append(Pizza(line['pizza_id'], line['pizza_type_id'], line['size'], float(line['price'])))
    
    # Extracting data from pizza_types.csv
    for line in DF_PIZZA_TYPES.iloc():
        id, cat, descript, ingr = line['pizza_type_id'], line['category'], line['name'], line['ingredients']
        for p in pizzas:
            if p.type_id == id:
                p._set_category_(cat)
                p._set_description_(descript)
                p._set_ingredients_(ingr)
    
    return pizzas

def _get_orders_() -> list[Order]:
    
    orders = []
    # Extracting data from orders.csv
    for line in DF_ORDERS.iloc():
        orders.append(Order(int(line['order_id']), time=(line['date'].split('/'), line['time'])))
    
    # Extracting data from order_details.csv
    orders_dict = {o.id: [] for o in orders}
    for line in DF_ORDER_DETAILS.iloc():
        id, count = line['pizza_id'], line['quantity']
        already_in = False
        hash = int(line['order_id'])
        if hash in orders_dict:
            for p in orders_dict[hash]:
                if p[0] == id:
                    already_in = True
                    p[1] += count
            if not already_in: orders_dict[hash].append([id, count])
    for order in orders:
        order: Order
        order._set_command_(orders_dict[order.id])

    return orders

def extract() -> list:
    '''
    Creating a list[Pizza] and and a list[Order] from the given MAVEN's data.
    '''

    print('·Extracting data...')
    pizzas = _get_pizzas_()
    orders = _get_orders_()
    print('<DONE>')

    return [pizzas, orders]

#TRANSFORM
def _get_ingredients_dict_(pizzas: list[Pizza]) -> dict:
    '''
    Setting the ingredients dictionary with the possible ingredients.
    All same type pizzas have the same ingredients, they just differ in the size
    '''

    ingredients_dict = {}
    indx = 0
    n_pizzas = len(pizzas)
    id = None
    while indx < n_pizzas:
        pizza = pizzas[indx]
        if pizza.type_id != id:
            for ingredient in pizzas[indx].ingredients:
                if not ingredients_dict.__contains__(ingredient): ingredients_dict[ingredient] = 0
        id = pizza.type_id
        indx += 1
    
    return ingredients_dict

def _buscar_pizza_id_(id: str, pizzas: list[Pizza]) -> Pizza:

    for p in pizzas:
        if p.id == id: return p
    
def _get_optimized_ingredients_(pizzas: list[Pizza], orders: list[Order], ingredients: dict) -> dict:
    '''
    Obtaining an optimized dict of ingredients based on the time of the year.
    Ingredients for every week of the month
    '''

    time_stamp = int(input('Month of the year for optimization of ingredients (1-12): '))
    for order in orders:
        if int(order.time[0][1]) == time_stamp:
            for p in order.command:
                quantity = order.command[p]
                pizza: Pizza = _buscar_pizza_id_(p, pizzas)
                for ing in pizza.ingredients: ingredients[ing] += (quantity*SIZE_MULTIPLIER[pizza.size])
    
    # The dictionary is optimized for the whole month. Let's reduce it to per the week
    n_weeks = MONTH_DAYS[time_stamp] * N_YEARS
    for ing in ingredients: ingredients[ing] = round(ingredients[ing]/n_weeks)

    return ingredients
    
def transform(pizzas: list[Pizza], orders: list[Order]) -> dict:
    '''
    Transforming extracted data.
    \nCalculating optimized ingedients list (for weekly consumery)
    '''

    print('·Transforming data...')
    ingredients = _get_ingredients_dict_(pizzas)
    optimized_ingredients = _get_optimized_ingredients_(pizzas, orders, ingredients)
    print('<DONE>')
    
    return optimized_ingredients

#LOAD
def load(optimized: dict, file_name: str='weekly_optimezed_ingredients.csv'):
    '''
    Loading obtained ingredients into a csv file.
    '''

    print(f'·Uploading to {file_name}...')
    file = open(file_name, 'w')
    file.write('ingredient,quantity\n')             #HEADER
    for ing in optimized:
        file.write(f'{ing},{optimized[ing]}'.strip() + '\n')     #line
    file.close()
    print('<DONE>')


def main(clear: bool=True):
    if clear: clear()
    pizzas, orders = extract()
    optimized_ingredients = transform(pizzas, orders)
    load(optimized_ingredients)


if __name__ == '__main__':

    main(clear=False)

    