# ============================================
# GUÍA Y EJERCICIOS - For y List Comprehension
# ============================================

# --------------------------------------------
# RECORDATORIO: ¿QUÉ ES UN FOR?
# Recorre una lista, elemento por elemento, y 
# repite un bloque de código para cada uno
# --------------------------------------------

# # Ejemplo 1: recorrer e imprimir
# frutas = ["manzana", "pera", "uva"]
# for fruta in frutas:
#     print(fruta)

# # Ejemplo 2: recorrer y sumar
# numeros = [10, 20, 30]
# total = 0
# for numero in numeros:
#     total = total + numero
# print(total)


# ============================================
# NIVEL BÁSICO
# ============================================

# Ejercicio 1: Recorre la lista "colores" e imprime cada uno 
# con el formato "Color: nombre"
print("==============EJERCICIO 1==================")

colores = ["rojo", "azul", "verde", "amarillo"]

for color in colores:
    
    print(f"Color: {color}")


#Ejercicio 2: Recorre la lista "precios" y calcula el total 
#(suma de todos)
print("==============EJERCICIO 2==================")

precios = [15000, 22000, 8000, 35000]

print(sum(precios))
    
    
# # Ejercicio 3: Recorre la lista "edades" y cuenta cuántas 
# # personas son mayores de edad (18 o más)
print("==============EJERCICIO 3==================")
edades = [15, 22, 17, 30, 12, 19]
contador = 0
for edad in edades:
        
    if edad >= 18:
        
        contador += 1
        
print(contador)        
        
    
# # Ejercicio 4: Recorre la lista "notas" y encuentra la nota 
# # más alta SIN usar la función max()
print("==============EJERCICIO 4==================")
notas = [3.5, 4.2, 2.8, 4.8, 3.9]

for nota in notas:
    
    if nota >= 4.5:
        
        print(nota)

# # Ejercicio 5: Crea una nueva lista "dobles" que contenga cada 
# # número de "numeros_base" multiplicado por 2
print("==============EJERCICIO 5==================")
numeros_base = [1, 2, 3, 4, 5]
dobles = []

for multi in numeros_base:
    
    totalMulti = multi * 2
    dobles.append(totalMulti)
    
print(dobles)

# # ============================================
# # NIVEL INTERMEDIO
# # ============================================

# # Ejercicio 6: Cuenta cuántas veces aparece el valor "manzana" 
# # en la lista "frutas_repetidas"
frutas_repetidas = ["manzana", "pera", "manzana", "uva", "manzana"]
contadorManzana = 0
print("==============EJERCICIO 6==================")

for fruta in frutas_repetidas:
    
    if fruta == "manzana":
        
        contadorManzana += 1
        
print(contadorManzana)

# # Ejercicio 7: Separa la lista "numeros_mixtos" en dos listas 
# # nuevas: "pares" e "impares"
print("==============EJERCICIO 7==================")

numeros_mixtos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []

for par in numeros_mixtos:
    if par % 2 == 0:
        
        pares.append(par)
        
    else:
        
        impares.append(par)
    
        
print(pares)
print(impares)

# # Ejercicio 8: Invierte el orden de la lista "orden_original"
# # Pista: pueden usar .reverse(), slicing [::-1], o investigar 
# # la función .insert() para hacerlo manualmente

print("==============EJERCICIO 8==================")

orden_original = ["a", "b", "c", "d", "e"]

orden_original.reverse()

print(orden_original)


# # Ejercicio 9: Combina "lista_a" y "lista_b" en una sola lista 
# # nueva llamada "combinada"
print("==============EJERCICIO 9==================")

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

combinada = lista_a + lista_b

print(combinada)

# # ============================================
# # NIVEL AVANZADO / RETO
# # ============================================

# # Ejercicio 10: Encuentra los valores que están repetidos en 
# # la lista "con_duplicados" (que aparezcan más de una vez)

print("==============EJERCICIO 10==================")
con_duplicados = [1, 2, 3, 2, 4, 5, 1, 6]

for repe in con_duplicados:
    
    
    
    


# # --------------------------------------------
# # LIST COMPREHENSION (forma corta de escribir un for)
# # --------------------------------------------

# numeros = [1, 2, 3, 4, 5]

# cuadrados_largo = []
# for n in numeros:
#     cuadrados_largo.append(n**2)

# cuadrados_corto = [n**2 for n in numeros]

# print(cuadrados_largo)
# print(cuadrados_corto)


# # Ejercicio 11: Usando list comprehension, crea una lista 
# # "positivos" que contenga solo los números mayores a 0 
# # de la lista "mixtos"
# mixtos = [-5, 3, -2, 8, -1, 10, 0]


# # Ejercicio 12 (reto): Usando list comprehension, crea una 
# # lista con el triple de cada número, pero SOLO de los 
# # números pares de "numeros_variados"
# numeros_variados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
