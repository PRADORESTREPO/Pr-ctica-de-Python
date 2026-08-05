#==============================#
#Sistema de domicilio - etapa 1
#==============================#
#print("Hola")


continuar = "s"

#distancia_en_m = a * distancia_km

while(continuar == "s"):

    distancia_km = float(input("Ingrese la distancia en Km: "))
    
    print(f"distancia en Km: {distancia_km}")


    if distancia_km <= 3:
            costo_domicilio = 3000

    elif distancia_km <= 8: 
            costo_domicilio = 7000

    else:
            costo_domicilio = 0

    if costo_domicilio == 0:
            print(f"Fuera del area de domicilio")
            
    else: 
            print(f"Costo del domicilio por Km es= ${costo_domicilio}")
            
    continuar = (input("Realizar otro calculo: (s/n)"))
    
    if continuar == "n":
       
        print("Gracias por utilizar el sistema")  
    
       
    
 
     
    
    
   
        
          
            
            
           




"""total_domicilio = costo_domicilio * distancia_km
print(f"Su costo total por el domicilio es:  {total_domicilio}")"""

