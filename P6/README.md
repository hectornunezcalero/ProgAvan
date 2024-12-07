# Preguntas y respuestas con la IA ChatGPT<br>

**Preg1:** ¿Qué ocurre si intentas agregar un objeto que no es ni un Empleado ni un Cliente al RegistroDiario?<br>
**Preg1:** No se agregará al registro porque el método agregar_persona valida el tipo del objeto y solo admite instancias de Empleado o Cliente​(registro_diario).

**Preg2:** ¿Cómo se determina si una persona es un Empleado dentro del RegistroDiario?<br>
**Preg2:** Se utiliza el método es_empleado, que verifica si el objeto es una instancia de la clase Empleado mediante isinstance​(registro_diario).

**Preg3:** ¿Qué sucede si accedes a un índice fuera del rango en el registro diario usando getitem?<br>
**Preg3:** Se lanza una excepción IndexError con el mensaje "Índice fuera de rango"​(registro_diario).

**Preg4:** ¿Qué formato se utiliza para mostrar la hora de nacimiento en la clase Ficha?<br>
**Preg4:** La hora de nacimiento se muestra en formato HH:MM:SS usando el método strftime​(ficha).

**Preg5:** ¿Qué ocurre al concatenar dos objetos de tipo RegistroDiario con el operador + ?<br>
**Preg5:**Se crea un nuevo RegistroDiario que contiene las personas de ambos registros combinados​(registro_diario).

**Preg6:** ¿Cómo se calcula el texto que devuelve Visualizar en la clase Empleado?<br>
**Preg6:** Combina el resultado de Visualizar en la clase base Ficha con los datos específicos del empleado, como Categoría y Antigüedad​(empleado).

**Preg7:** ¿Qué valor toma el atributo _nacio en la clase Ficha si no se especifica al crear una instancia?<br>
**Preg7:**Por defecto, _nacio toma el valor 00:00:00, definido como time(0, 0, 0)​(ficha).