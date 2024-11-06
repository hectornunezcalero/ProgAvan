def operation_logger(func):
    # Decorador que registra el nombre de la operación, entradas y resultado.
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Operación: {func.__name__}, Entradas: {args}, Resultado: {result}")
        return result
    return wrapper

add = lambda *args: sum(args)  # Función lambda para la suma de números.
subtract = lambda *args: args[0] - sum(args[1:])  # Función lambda para la resta de números.
multiply = lambda *args: 1 if not args else args[0] * multiply(*args[1:])  # Función lambda para la multiplicación de números.
divide = lambda x, y: x / y if y != 0 else "Error: División por cero"  # Función lambda para la división de números.

@operation_logger
def math_operation(operation, *args, **kwargs):
    # Realiza una operación matemática usando la función lambda dada.
    return operation(*args, **kwargs)

# Pruebas
print(math_operation(add, 5, 3))
print(math_operation(subtract, 10, 4))
print(math_operation(multiply, 2, 6))
print(math_operation(divide, 15, 3))
print(math_operation(divide, 10, 0))  # Manejo de división por cero
print(math_operation(add, 1, 2, 3, 4, 5))  # Manejo de múltiples argumentos
