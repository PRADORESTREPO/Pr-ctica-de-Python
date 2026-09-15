# ============================================
# EJERCICIOS - Funciones en Python
# ============================================

# --------------------------------------------
# NIVEL BÁSICO
# --------------------------------------------

# Ejercicio 1: Crea una función llamada "saludar_usuario" que 
# reciba un nombre como parámetro, y muestre "Bienvenido, [nombre]"
def saludar_usuario(nombre):
    print(f"Bienvenido, {nombre}")


# Ejercicio 2: Crea una función "es_mayor_edad" que reciba una edad 
# y devuelva (return) True si es mayor o igual a 18, o False si no
def es_mayor_edad(edad):
    return edad >= 18


# Ejercicio 3: Crea una función "calcular_precio_con_iva" que 
# reciba un precio y devuelva ese precio con el 19% de IVA agregado
def calcular_precio_con_iva(precio):
    return precio * 1.19


# --------------------------------------------
# NIVEL INTERMEDIO
# --------------------------------------------

# Ejercicio 4: Crea una función "contar_vocales" que reciba una 
# palabra y devuelva cuántas vocales tiene
def contar_vocales(palabra):
    contador = 0
    for letra in palabra.lower():
        if letra in "aeiou":
            contador += 1
    return contador


# Ejercicio 5: Crea una función "buscar_en_lista" que reciba una 
# lista y un valor a buscar, y devuelva True si el valor está en 
# la lista, o False si no
def buscar_en_lista(lista, valor):
    return valor in lista


# Ejercicio 6: Crea una función "promedio" que reciba una lista de 
# números y devuelva el promedio (usa sum() y len())
def promedio(numeros):
    return sum(numeros) / len(numeros)


# --------------------------------------------
# NIVEL AVANZADO
# --------------------------------------------

# Ejercicio 7: Crea una función "filtrar_mayores" que reciba una 
# lista de números y devuelva una nueva lista solo con los 
# números mayores a 50
def filtrar_mayores(numeros):
    return [n for n in numeros if n > 50]


# Ejercicio 8 (con valor por defecto): Crea una función 
# "generar_descuento" que reciba un precio y un porcentaje de 
# descuento (por defecto 10%), y devuelva el precio ya descontado
def generar_descuento(precio, porcentaje=10):
    return precio - (precio * (porcentaje / 100))


# --------------------------------------------
# APLICADO A TU PROYECTO
# --------------------------------------------

# Ejercicio 9: Opción de eliminar producto convertida en función simple
def eliminar_producto(inventario):
 
    try:
        remover = input("\nIngrese el producto que quiere remover del stock: ").strip().lower()

        if not remover:
            print(" El nombre del producto a remover no puede estar vacío.")
        elif remover in inventario:
            del inventario[remover]
            print(f" Se ha eliminado '{remover.capitalize()}' del inventario.")
        else:
            print(f" El producto '{remover.capitalize()}' no existe en el stock.")

    except KeyError as ke:
        print(f" Error de palabra clave al intentar eliminar: {ke}")
    except Exception as e:
        print(f" Error inesperado al intentar eliminar el producto: {e}")



# Ejercicio 10 (reto): Opción de buscar producto usando return
def buscar_producto(inventario):

    try:
        busqueda = input("\nIngrese el producto que quiere buscar: ").strip().lower()

        if not busqueda:
            print(" El término de búsqueda no puede estar vacío.")
        elif busqueda in inventario:
            print(f"-> Stock de {busqueda.capitalize()}: {inventario[busqueda]} unidad(es)")
        else:
            print(f" El producto '{busqueda.capitalize()}' no se encuentra en el stock.")

        input("\nPresione ENTER para volver al menú principal...")
    except KeyboardInterrupt:
        print("\n Búsqueda cancelada.")
    except Exception as e:
        print(f" Error inesperado durante la búsqueda: {e}")