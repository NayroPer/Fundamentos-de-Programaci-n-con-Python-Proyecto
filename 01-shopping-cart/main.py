# Simulador de Tienda con Carrito de Compras
from typing import Dict
# Lista de productos precargados al sistema


productos_almacenados: Dict[str,dict] = {
                    "P001":{"precio":12.00,"nombre":"CABLE"},
                    "P002": {"precio": 0.75, "nombre": "BATERIA"},
                    "P003": {"precio": 1.25, "nombre": "PILA"},
                    "P004": {"precio": 3.50, "nombre": "RELOJ"},
                    "P005": {"precio": 2.00, "nombre": "CUADERNO"},
                    }


# Lista de productos en el carrito

carrito: Dict[str,dict] = {
                        "P004":{"cantidad":2},
                        "P005":{"cantidad":2}
                        }

# Funciones 

def ver_catalogo():
    print("Lista de productos: ")
    print("---"*10)
    for codigo, detalles in productos_almacenados.items():
        precio = detalles["precio"]
        nombre = detalles["nombre"]
        print(f"​✔️​​  {codigo} {nombre}, precio {precio:.2f}")
        print("---"*10)

def ver_carrito():

    print("---"*10)
    monto_total = 0
    for codigo_c,cantidades in carrito.items():
        cantidad=cantidades["cantidad"]
        for codigo_a, detalles in productos_almacenados.items():
            if codigo_a == codigo_c:
                precio = detalles["precio"]
                nombre = detalles["nombre"]
                print(f"​🏷️​​- {nombre} (x{cantidad})-> "+"S/"+ str(cantidad*precio))
                monto_total += cantidad*precio
    print("💰 Monto Total: S/ " + str(monto_total))
    
def agregar_producto(producto : str,cantidad_a_agregar : int)->None:
    if  producto not in carrito:
        carrito[producto]={"cantidad": cantidad_a_agregar}
    else:
        carrito[producto]["cantidad"] += cantidad_a_agregar
    print("Producto agregado al carrito. ✔️✔️​")

def eliminar_producto(id_producto: str):
    
    for codigo,detalles in productos_almacenados.items():
        if id_producto==codigo:
            nombre=detalles["nombre"]
    del carrito[id_producto]
    print(f"❌ Se elimino el {nombre} del carrito de compras❌")

def vaciar_carrito():
    carrito.clear()
    
    
def finalizar_compra():
    print("📑 Resumen de la compra:")
    ver_carrito()
    vaciar_carrito()
    print(" 🧾Gracias por tu compra ✅✅")
    

def Menu():
    ver_menu()
    estado: bool = True
    while estado:
        opcion = int(input())
        if opcion == 1:
            ver_catalogo()
        elif opcion == 2:
            estado_añadir: bool = False
            while not estado_añadir: 
                # Id_producto
                estado_agregar: bool = False
                while not estado_agregar: 
                    try:   
                        id_producto,estado_agregar = validar_codigo()
                    except Exception as e:
                            print(f"{e}")  
                # Cantidad
                estado_cantidad: bool = False
                while not estado_cantidad:   #mientras no ingresa un entero el buble continua
                    try:
                        cantidad,estado_cantidad = validar_cantidad() # Validamnos si es un entero
                    except Exception as e:
                        print(f"{e}")
                        
                agregar_producto(id_producto,cantidad)
                ver_carrito()
                adicionar_productos = str(input("Deseas Agregar más productos al carrito de compras ⁉️ (S = si / Cualquier tecla se entendera como un NO) ?\n")).upper()
                if not adicionar_productos == 'S':                      
                    estado_añadir=True
                    ver_menu()
        
        elif opcion == 3:
            
            estado_eliminar: bool = False
            while not estado_eliminar:
                try:
                    id_producto,estado_eliminar=validar_eliminar()
                except Exception as e:
                            print(f"{e}")  
            eliminar_producto(id_producto)
            ver_carrito()
            ver_menu()
                    
        elif opcion == 4:
            vaciar_carrito()
            print("⚠️​ Se vacio el carrito de compras.⚠️​")
            ver_menu()
            
        elif opcion == 5:
            print("🛒 Productos en el Carrito de compras: 🛒​")
            ver_carrito()
            ver_menu()
            
        elif opcion == 6:
            finalizar_compra()
            ver_menu()
            
        elif opcion == 7:
            estado = False
            print("​👋​ Hasta pronto ​👋​")

# Menu
def ver_menu():
    print("🏪 MENU 🏪 \n ¿Qué deseas hacer?\n \n"
          + "1. Ver catálogo\n"
          + "2. Agregar producto al carrito\n"
          + "3. Eliminar producto del carrito\n"
          + "4. Vaciar carrito\n "
          + "5. Mostrar carrito\n "
          + "6. Finalizar compra\n "
          + "7. Salir" ) 
    
# Funciones de Validacion

def validar_cantidad() -> bool:
    cantidad = input("Cantidad: ")
    if not cantidad.isdigit():
        raise Exception("La cantidad deberia ser un número ⚠️")
    return int(cantidad),True

def validar_codigo ()->str:
    id_producto=str(input("Ingrese el código de producto:\n")).upper()
    if id_producto not in productos_almacenados: # Validamos si el codigo existe
        raise Exception("⚠️  El código de producto NO se existe !! ⚠️​")
    
    return id_producto,True

def validar_eliminar ()->str:
    id_producto=str(input("Ingrese el código del producto que desea eliminar‼️ \n")).upper()
    if id_producto not in carrito: # Validamos si el codigo existe en el carrito
        raise Exception("⚠️El Producto NO se encuentra en el carrito​ de compras⚠️​")
    return id_producto,True

Menu()