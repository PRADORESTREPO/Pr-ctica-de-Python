saberColorSemaforo = input("¿Quieres ver que significa el color actual del semaforo?: (s/n)")

while(saberColorSemaforo == "s"):
    semaforoColor =input("Diga el color del semaforo entre (verde/amarillo/rojo)")
    
    if semaforoColor == "rojo":
        
        print("Los vehiculos deben parar")
        
        
    elif semaforoColor == "amarillo":
        
        print("Los vehiculos deben ir despacio")
        
        
    else: 
        print("Los vehiculos deben avanzar")
        
        
    continuar = input("¿Desea utilizar de nuevo el sistema? (s/n)")   
    if continuar == "n": 
    
        print("Gracias por utilizar el sistema")
        break
        
    

    