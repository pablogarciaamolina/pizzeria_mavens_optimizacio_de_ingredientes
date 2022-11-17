Recibimos un nuevo set de datos en formato erroneo, es decir, no puede ser utilizado nuestro algoritmo
para carcular la lista de ingredientes a comprar.

<br>Añadiremos un formateo de los datos para tarnsformarlos a un formato valido.<br>

<br>FORMATO VALIDO:<br>

<br>order_details_id: entero en formato str. El dataset puede estar ordenado en funcion de este pero no es necesario<br>
order_id: entero en formato str.<br>
<br>pizza_id: str en minúscolas y usando snake_case. No se admiten carancteres especiales (aparte de _) ni tildes.<br>
<br>date: en formato DD/MM/YY. Si no se incluye informacion en este campo, se descartara la orden.<br>
<br>time: en formato HH:MM:SS. Este campo realmente no es necesario para el algoritmo.<br>