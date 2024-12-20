# Preguntas y respuestas con la IA ChatGPT<br>

**Preg1:** Por qué usamos @property en lugar de acceder directamente a los atributos?<br>
**Preg1:** Para encapsular los atributos y permitir validaciones o lógica adicional al acceder o modificar valores.

**Preg2:** ¿Cómo sabe cargar_publicaciones si debe crear un Libro o una Revista?<br>
**Preg2:** Detecta claves específicas (_genero para Libro, _num_edicion para Revista) en los datos cargados del archivo JSON.

**Preg3:** ¿Por qué usamos super().__init__() en las clases derivadas?<br>
**Preg3:** Para inicializar los atributos de la clase base (Publicacion) sin reescribir su constructor.

**Preg4:** ¿Qué hace ErrorArchivo que no haga una excepción estándar como FileNotFoundError?<br>
**Preg4:** Permite personalizar el mensaje de error y mantener una jerarquía de excepciones específica para la biblioteca.

**Preg5:** ¿Cómo convierte guardar_publicaciones las instancias en datos JSON?<br>
**Preg5:** Usa __dict__ para acceder a los atributos como un diccionario y luego los guarda con json.dump().

**Preg6:** ¿Por qué el programa principal usa match en lugar de if-elif?<br>
**Preg6:** match es más legible y compacto para manejar múltiples casos basados en valores específicos.

**Preg7:** ¿Qué pasa si el archivo JSON cargado tiene un formato incorrecto?<br>
**Preg7:** Se lanza una excepción ErrorArchivo personalizada, indicando que el formato no es válido.