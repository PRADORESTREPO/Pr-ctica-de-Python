edadDelUsuario = int(input("Ingrese la edad del usuario que quiere adquirir la boleta: "))

diasDeAnticipacionDeCompra = int(input("Ingrese los dias de anticipacion con los cuales compra la boleta: "))
if edadDelUsuario >= 18 and diasDeAnticipacionDeCompra >= 7:
    suEntradaEs = "Su acceso es VIP"
elif edadDelUsuario >= 18 or diasDeAnticipacionDeCompra >= 7:
    suEntradaEs = "Su acceso es General"
else:
    
    suEntradaEs = "Sin acceso"

print(f"Su nivel de acceso es: {suEntradaEs}")

