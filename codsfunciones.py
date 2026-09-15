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


saludar_usuario("Ana")

print("_______________________________________________")
# Ejercicio 2: Crea una función "es_mayor_edad" que reciba una edad 
# y devuelva (return) True si es mayor o igual a 18, o False si no
def es_mayor_edad(edad):
    return edad >= 18


print("¿Es mayor de edad (18)?:", es_mayor_edad(18))
print("¿Es mayor de edad (15)?:", es_mayor_edad(15))

print("_______________________________________________")
# Ejercicio 3: Crea una función "calcular_precio_con_iva" que 
# reciba un precio y devuelva ese precio con el 19% de IVA agregado
def calcular_precio_con_iva(precio):
    return precio * 1.19


precio_final = calcular_precio_con_iva(100)
print(f"Precio final con IVA (19%): ${precio_final}")

print("_______________________________________________")
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


total_vocales = contar_vocales("Programacion")
print(f"Cantidad de vocales en 'Programacion': {total_vocales}")

print("_______________________________________________")
# Ejercicio 5: Crea una función "buscar_en_lista" que reciba una 
# lista y un valor a buscar, y devuelva True si el valor está en 
# la lista, o False si no
def buscar_en_lista(lista, valor):
    return valor in lista


frutas = ["manzana", "peras", "uva"]
print("¿'manzana' está en la lista?:", buscar_en_lista(frutas, "manzana"))
print("¿'lulo' está en la lista?:", buscar_en_lista(frutas, "lulo"))

print("_______________________________________________")
# Ejercicio 6: Crea una función "promedio" que reciba una lista de 
# números y devuelva el promedio (usa sum() y len())
def promedio(numeros):
    return sum(numeros) / len(numeros)


notas = [4.5, 3.8, 5.0, 4.0]
print(f"El promedio de las notas es: {promedio(notas)}")

print("_______________________________________________")
# --------------------------------------------
# NIVEL AVANZADO
# --------------------------------------------

# Ejercicio 7: Crea una función "filtrar_mayores" que reciba una 
# lista de números y devuelva una nueva lista solo con los 
# números mayores a 50
def filtrar_mayores(numeros):
    return [n for n in numeros if n > 50]


lista_valores = [20, 55, 10, 80, 50, 99]
print("Números mayores a 50:", filtrar_mayores(lista_valores))

print("_______________________________________________")
# Ejercicio 8 (con valor por defecto): Crea una función 
# "generar_descuento" que reciba un precio y un porcentaje de 
# descuento (por defecto 10%), y devuelva el precio ya descontado
def generar_descuento(precio, porcentaje=10):
    return precio - (precio * (porcentaje / 100))


print("Descuento por defecto (10% de $1000):", generar_descuento(1000))
print("Descuento personalizado (20% de $1000):", generar_descuento(1000, 20))

print("_______________________________________________")
# --------------------------------------------
# APLICADO A TU PROYECTO
# --------------------------------------------


mi_inventario = {"arroz": 10, "frijoles": 5}

# Ejercicio 9
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

eliminar_producto(mi_inventario)

print("_______________________________________________")
# Ejercicio 10 
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

buscar_producto(mi_inventario)