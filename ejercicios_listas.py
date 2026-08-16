# ============================================
# EJERCICIOS - Listas en Python
# Escribe tu código debajo de cada enunciado
# ============================================

# --------------------------------------------
# ACTIVIDAD 1: Explica con tus palabras qué hace 
# cada línea, agregando un comentario arriba de cada una
# --------------------------------------------

#Crea una variable la cual esta designada como "notas" y la asignacion son unos corchetes que significan que es una lista
notas = []

#Pide al usuario que ingrese una nota
nota1 = float(input("Ingresa una nota: "))

#La nota que haya ingresado el usuario pasara y se agregara al fondo de la lista
notas.append(nota1)

#Imprime todas las notas que se agregaron a la lista designada como "notas"
print(f"Total de notas: {notas}")


# --------------------------------------------
# EJERCICIO 1
# Crea una lista vacía llamada "temperaturas".
# Pide 3 temperaturas al usuario (una por una) y 
# agrégalas a la lista. Al final, imprime la temperatura 
# más alta y la más baja (usa max() y min())
# --------------------------------------------

temperaturasLista = []
continuar = "s"

while continuar == "s" :
    
    temperaturas = input(f"Ingrese 3 temperaturas:")
    temperaturasLista.append(temperaturas)
    
    continuar = input(f"¿Ingresar otra temperatura? (s/n)")
    
print(max(temperaturasLista))
print(min(temperaturasLista))


# --------------------------------------------
# EJERCICIO 2
# Crea una lista con 5 nombres de compañeros.
# Recorre la lista e imprime cada nombre con un saludo, 
# ejemplo: "Hola, Juan!"
# --------------------------------------------

nombreCompañeros = ["Jhoan", "Camila", "Valeria", "Angel", "Victor"]

for saludoCadaCompañero in nombreCompañeros:
    print(f"Hola, {saludoCadaCompañero}")


# --------------------------------------------
# RETO OPCIONAL (para quien quiera ir más allá)
# Usando list comprehension, crea una lista nueva 
# que contenga solo las temperaturas mayores a 20 grados 
# de tu lista "temperaturas" del Ejercicio 1
# --------------------------------------------

temperaturaAlta = [temp for temp in temperaturasLista if temp > 20 ] 


print(f"Los valores que son mayores a 20°: {temperaturaAlta}")
print(max(temperaturaAlta))
print(min(temperaturaAlta))




