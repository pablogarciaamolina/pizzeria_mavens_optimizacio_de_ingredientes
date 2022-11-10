Recibimos un nuevo set de datos en formato erróneo, es decir, no puede ser utilizado nuestro algoritmo
para carcular la lista de ingredientes a comprar.

Añadiremos un formateo de los datos para tarnsformarlos a un formato válido.

FORMATO VALIDO:

order_details_id: entero en formato str. El dataset puede estar ordenado en función de este pero no es necesario
order_id: entero en formato str.
pizza_id: str en minúscolas y usando snake_case. No se admiten carancteres especiales (aparte de _) ni tildes.
date: en formato DD/MM/YY. Si no se incluye información en este campo, se descartará la orden.
time: en formato HH:MM:SS. Este campo realmente no es necesario para el algoritmo.