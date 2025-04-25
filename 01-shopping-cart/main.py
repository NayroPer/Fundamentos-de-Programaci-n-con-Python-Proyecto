 # Simulador de Tienda con Carrito de Compras
 
 # Lista de productos precargados al sistema
productos_almacenados={
                    "P001":{"precio":12.00,"nombre":"CABLE"},
                    "P002": {"precio": 0.75, "nombre": "BATERIA"},
                    "P003": {"precio": 1.25, "nombre": "PILA"},
                    "P004": {"precio": 3.50, "nombre": "RELOJ"},
                    "P005": {"precio": 2.00, "nombre": "CUADERNO"},
                    }
# Lista de productos en el carrito
carrito ={"P004":{"cantidad":2},
          "P005":{"cantidad":2}}
def ver_catalogo():
    print("Lista de productos: ")
    print("---"*10)
    for codigo, detalles in productos_almacenados.items():
        precio = detalles["precio"]
        nombre = detalles["nombre"]
        print(f"​✔️​​  {codigo} {nombre}, precio {precio:.2f}")
        print("---"*10)

def mostrar_carrito():
    print("🛒 Productos en el Carrito de compras: 🛒​")
    print("---"*10)
    monto_total=0
    for codigo_c,cantidades in carrito.items():
        cantidad=cantidades["cantidad"]
        for codigo_a, detalles in productos_almacenados.items():
            if codigo_a == codigo_c:
                precio = detalles["precio"]
                nombre = detalles["nombre"]
                print(f"​🏷️​​- {nombre} (x{cantidad})-> "+"S/"+ str(cantidad*precio))
                monto_total+= cantidad*precio
    print("💰 Monto Total: S/ " + str(monto_total))
    
def agregar_al_carrito(producto,cantidad_a_agregar):
    if not producto in carrito:
        carrito[producto]={"cantidad": cantidad_a_agregar}
    else:
        carrito[producto]["cantidad"]+= cantidad_a_agregar
    #return True
    print("✔️​ Producto agregado al carrito.")

def eliminar_del_carrito():
    return True

def vaciar_productos(producto)->bool:
    return True 

def finalizar_compra(producto)->bool:
    return True

def loop_de_ejecuccion():
    print("Bienvenido a la Tienda Virtual \n ¿Qué deseas hacer?\n \n 1. Ver catálogo\n 2. Agregar producto al carrito\n 3. Eliminar producto del carrito\n 4. Vaciar carrito\n 5. Mostrar carrito\n 6. Finalizar compra\n 7. Salir")
    estado = True
    while estado:
        opcion=int(input())
        if opcion==1:
            ver_catalogo()
        elif opcion == 2:
            """ agregar =0
            while agregar:"""
            producto=str(input("Ingrese el código de producto: ")).upper()
            cantidad=int(input("Cantidad: "))
            agregar_al_carrito(producto,cantidad)
            
        elif opcion == 3:
            eliminar_producto()
        elif opcion == 4:
            carrito.clear()
            print("⚠️​ Se vacio el carrito de compras.⚠️​")
        elif opcion == 5:
            mostrar_carrito()
        elif opcion == 6:
            finalizar_compras()
        elif opcion == 7:
            estado = False
            print("​👋​ Hasta pronto ​👋​")
    
loop_de_ejecuccion()