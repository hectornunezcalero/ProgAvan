# Preguntas y respuestas propuestas a la IA ChatGPT:

# Ejercicio 1.

Preg1: ¿qué intervalos coge range si pongo range(1, 6)?
Resp1: range cuenta desde el 1 incluido hasta el 6 sin incluir

Preg2: ¿Es lo mismo poner continue que exit?
Resp2: No. continue sale de una condición y exit() del programa entero.

Preg3: ¿Y la diferencia entre continue y break cuál es?
Resp3: continue se usa para salir de una condición y break para salir de un bucle (if/for).

# Ejercicio 2.

Preg1: ¿Hay otra manera de expresar 'word.lower() for word in words_to_replace'?
Resp1: Sí:
for word in words_to_replace:
  word_lower = word.lower()

Preg2: Cuál es la diferencia de hacer el 'for word in text' con .split() al final?
Resp2: Se añade .split() para que se cuenten las palabras y sin .split() se cuentan las letras.

Preg3: ¿Estás de acuerdo con que la parte más importante del código es el .replace?
Resp3: Sí, porque es lo que hace cambiar la palabra por asteriscos, cubriendo todas las letras.

# Ejercicio 3.

Preg1: ¿Cómo has realizado la operación de los números primos?
Resp1: Contando que el número es mayor que 1, se comprueba si el número a probar es divisible desde por 2 hasta su raíz + 1 (ya que range no incluye el último número, es decir, su raíz). Así pasaremos el filtro de si es o no un número primo.

Preg2: ¿'.append' mete directamente los números seguidos con comas?
Resp2: Sí.

Preg3: 


