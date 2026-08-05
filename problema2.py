print(f"Se esta dando un premio a los clientes por comprar 5 o mas productos")
numeroProductosCliente = int(input("Por favor digite cuantos productos compro: "))
mensajeGanador = "====Ganaste un premio por tus compras===="
if numeroProductosCliente >= 5:

        print(mensajeGanador)
        
else:
    print("====No ganaste, vuelve a intentarlo para la proxima====")