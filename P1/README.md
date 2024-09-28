# Preguntas y respuestas propuestas a la IA ChatGPT:

# Ejercicio 1.

Preg1: ¿qué intervalos coge range si pongo range(1, 6)?<br>
Resp1: range cuenta desde el 1 incluido hasta el 6 sin incluir

Preg2: ¿Es lo mismo poner continue que exit?<br>
Resp2: No. continue sale de una condición y exit() del programa entero.

Preg3: ¿Y la diferencia entre continue y break cuál es?<br>
Resp3: continue se usa para salir de una condición y break para salir de un bucle (if/for).

# Ejercicio 2.

Preg1: ¿Hay otra manera de expresar 'word.lower() for word in words_to_replace'?<br>
Resp1: Sí:<br>
for word in words_to_replace:<br>
  <div>word_lower = word.lower()

Preg2: Cuál es la diferencia de hacer el 'for word in text' con '.split()' al final?<br>
Resp2: Se añade '.split()' para que se cuenten las palabras y sin '.split()' se cuentan las letras.

Preg3: ¿Estás de acuerdo con que la parte más importante del código es el '.replace'?<br>
Resp3: Sí, porque es lo que hace cambiar la palabra por asteriscos, cubriendo todas las letras.

# Ejercicio 3.

Preg1: ¿Cómo has realizado la operación de los números primos?<br>
Resp1: Contando que el número es mayor que 1, se comprueba si el número a probar es divisible desde por 2 hasta su raíz + 1 (ya que range no incluye el último número, es decir, su raíz). Así pasaremos el filtro de si es o no un número primo.

Preg2: ¿'.append' mete directamente los números seguidos con comas?<br>
Resp2: Sí.

Preg3: ¿Qué hace exactamente 'str' y por qué es necesario?<br>
Resp3: 'str' convierte el número en cadena, y es necesario para comparar dos cadenas, aunque estemos tratando con números en el ejercicio.

Preg4: ¿Me puedes explicar la sintaxis '[::-1]'?<br>
Resp4: Significa '[start:stop:step]' donde  'start' es el comienzo, 'stop' el final (sin incluir) y 'step' el método de avance.
Dado que 'start' y 'stop' están vacíos, se coge toda la cadena 'str(prime)' y se avanza de detrás a adelante (-1) en vez de delante a detrás. 'str(prime)' sin '[ ]' indica que se coge toda la cadena de delante a detrás.

Preg5: ¿Cuál es el método clave para añadir en un diccionario una lista elemento a elemento?<br>
Resp5: 'categorized_primes[category].append(prime)'.

Preg6: Explícame qué hace esta parte de código en la que imprime los tamaños de números primos:<br>
for category, numbers in categorized_primes.items():<br>
  <div>print(f"{category.capitalize()}: {numbers}")<br>
Resp6: Es un iterador de pares clave-valor para el diccionaro 'categorized_primes'.

Preg7: ¿Y qué hace 'category.capitalize()'?<br>
Resp7: Es un método que convierte la primera letra de la categoría en mayúscula y el resto en minúscula. Para que, por ejemplo, 'pequeños:' se convierta en 'Pequeños:'.

Preg8: ¿Qué puedo cambiar si quiero que el límite de números primos sea elegido por el usuario?<br>
Resp8: Puedes añadir un 'input()' y que el límite sea <= 2.


