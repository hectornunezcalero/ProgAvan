# Decorador para registrar operaciones
def operation_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        operation_name = func.__name__
        print(f"Operación: {operation_name}, Entradas: {args}, Resultado: {result}")
        return result
    return wrapper

# Funciones lambda para operaciones matemáticas
add = lambda *args: sum(args)
subtract = lambda x, y: x - y
multiply = lambda *args: 1 if len(args) == 0 else args[0] * multiply(*args[1:])
divide = lambda x, y: x / y if y != 0 else 'Error: División por cero'

# Función para realizar operaciones matemáticas
@operation_logger
def math_operation(operation, *args):
    return operation(*args)

# Pruebas
print(math_operation(add, 5, 3))
print(math_operation(subtract, 10, 4))
print(math_operation(multiply, 2, 6))
print(math_operation(divide, 15, 3))
print(math_operation(divide, 10, 0))  # Manejo de división por cero
print(math_operation(add, 1, 2, 3, 4, 5))  # Múltiples argumentos
