class ErrorBiblioteca(Exception):
    def __init__(self, mensaje="Error en la biblioteca"):
        super().__init__(mensaje)


class ErrorArchivo(ErrorBiblioteca):
    def __init__(self, mensaje="Error relacionado con archivos"):
        super().__init__(mensaje)
