# Preguntas y respuestas con la IA ChatGPT<br>

**Preg1:** ¿Qué acciones con matrices nos permite la librería numpy?<br>
**Resp1:** NumPy permite crear, manipular, sumar, restar, multiplicar y realizar operaciones algebraicas con matrices, así como aplicar funciones matemáticas y estadísticas.

**Preg2:** ¿Cómo podría poner de otra manera la expresion return self._Matriz is not None? <br>
**Resp2:** Podrías usar return bool(self._Matriz) para obtener el mismo resultado, ya que convertirá el valor de _Matriz en un booleano.

**Preg3:** ¿Qué hace .shape?<br>
**Resp3:** .shape devuelve las dimensiones de un array de NumPy como una tupla, indicando el número de filas y columnas en el caso de matrices.

**Preg4:** ¿la posibilidad de realizar esta suma depende de numpy? return self._Matriz + otra_matriz._Matriz. Si es así, ¿cuál sería la solución sin usar numpy?<br>
**Resp4:** Sí, la suma self._Matriz + otra_matriz._Matriz utiliza la funcionalidad de NumPy para realizar la operación elemento a elemento entre arrays. Para hallar la solución sin numpy, habría que operar número a número mediante los índices 'i' y 'j' 

**Preg5:** ¿Cuál es la funcionalidad de enumerate aquí? for i, opcion in enumerate(opciones_menu, 1):<br>
**Resp5:** enumerate permite iterar sobre opciones_menu, proporcionando tanto el índice (empezando desde 1) como el valor de cada elemento, lo que facilita mostrar un menú numerado.

**Preg6:** ¿Cuál sería la equivalencia usando range?<br>
**Resp6:** for i in range(len(opciones_menu)): <br>   print(f"{i + 1}. {opciones_menu[i]}")

**Preg7:** ¿Cuál es el número máximo de columnas/filas que me permite este programa utilizar?<br>
**Resp7:** 
El programa no establece un límite explícito para el número de filas y columnas, por lo que está limitado únicamente por la memoria disponible del sistema. En teoría, puedes crear matrices tan grandes como la memoria lo permita.