# Preguntas y respuestas con la IA ChatGPT<br>

**Preg1:** ¿Cómo funciona el decorador operation_logger?<br>
**Preg1:** El decorador envuelve una función, ejecuta su lógica (en este caso, registrar el nombre de la función, sus argumentos y su resultado) y luego devuelve el resultado original de la función decorada.

**Preg2:** ¿Cómo funciona la recursividad en la función multiply?<br>
**Preg2:** La lambda multiply llama a sí misma (multiply(*args[1:])) para multiplicar el primer argumento con el resultado de multiplicar el resto, usando la condición base 1 if not args para detenerse cuando no hay más argumentos.

**Preg3:** ¿Cómo se maneja la división por cero en la función divide?<br>
**Preg3:** La lambda divide verifica si el divisor (y) es 0. Si es 0, devuelve un mensaje de error ("Error: División por cero"); si no, realiza la división normalmente (x / y).

**Preg4:** ¿Cómo se asegura la unicidad de los IDs de usuarios y libros?<br>
**Preg4:** El módulo uuid genera identificadores únicos mediante la función uuid4(). En el archivo utils.py, la función generar_id_unico() crea un ID de 8 caracteres usando str(uuid4())[:8]. Esto garantiza un alto grado de unicidad debido al diseño aleatorio de UUID versión 4.

**Preg5:** ¿Cómo se maneja el estado de un libro para saber si está disponible o prestado?<br>
**Preg5:** En el archivo book.py, cada instancia de Book tiene un atributo booleano is_borrowed. Cuando un libro se presta, este atributo se establece en True. Al devolver el libro, se cambia a False. La clase Library utiliza este atributo en métodos como borrow_book y return_book para validar la operación.

**Preg6:** ¿Cómo se evita que un usuario preste más libros de los que puede manejar?<br>
**Preg6:** En el archivo user.py, cada instancia de User tiene una lista borrowed_books que contiene los libros prestados. Antes de añadir un libro, se podría implementar una validación para limitar el número máximo de préstamos permitidos (aunque esto debe agregarse explícitamente si no está en el código).

**Preg7:** ¿Qué sucede si se intenta prestar un libro inexistente o ya prestado?<br>
**Preg7:**En el archivo library.py, el método borrow_book verifica si el libro con el ISBN dado está en la lista de libros y si is_borrowed es False. Si no se encuentra el libro o ya está prestado: Devuelve None, lo que permite al programa principal mostrar un mensaje adecuado al usuario. Esto asegura que no se produzcan errores al intentar prestar un libro no disponible.