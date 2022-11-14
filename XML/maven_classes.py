'''
Clases de Pizza() y Orden() para gestionar las pizzas y órdenes de la pizzaeria MAVEN
'''

import inspect
from dataclasses import dataclass, field
from pprint import pprint

@dataclass(frozen=False)
class Pizza:
    id: str = field()
    type_id: str = field()
    size: str = field()
    price: float = field()
    category: str = field(default='')
    description: str = field(default='')
    ingredients: list[str] = field(default_factory=list)

    def _set_category_(self, message: str) -> None:
        self.category = message

    def _set_description_(self, message: str) -> None:
        self.description = message
    
    def _set_ingredients_(self, raw_ingredients: str) -> None:
        self.ingredients = raw_ingredients.split(',')

@dataclass
class Order:
    id: int = field()
    time: tuple = field(default=None)
    command: dict = field(default_factory=dict)

    def _set_time_(self, date, time) -> None:
        time = (date, time)
    
    def _set_command_(self, check: list[list]) -> None:
        '''
        -> check: list containing lists such that [<pizza_id>, number of <pizza_id>]
        '''
        for line in check:
            self.command[line[0]] = int(line[1])