print(f"El valor de la boleta general es de 8000 y si eres estudiante tiene el 20% de descuento")
estudiante = input("¿Eres estudiante? Responde (s/n)")
precioEstudiante = "s"
precioGeneral = 0
if estudiante == "s": 
    
    precioEstudiante = 8000 * 0.20
    precioDescuento = int(8000 - precioEstudiante)
    print(f"El precio de tu boleta como estudiante es de: {precioDescuento}")
else:
    
    precioGeneral = 8000
    print(f"Su boleta como cliente general es a: {precioGeneral}")
    
    
    
    
    
    