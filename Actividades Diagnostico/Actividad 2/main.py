import collections
import os

if __name__ == "__main__":
    carpeta = input("Ingrese nombre de carpeta: ")
    productos_path = os.path.join(carpeta, "productos.txt")
    acciones_path = os.path.join(carpeta, "acciones.txt")
    inventario = []
    rut_lista = []
    rut_index = []
    index_producto = []

    # Aqui se leen los productos
    # Por completar: Crear inventario
    with open(productos_path, "r") as productos_file:
        for producto_line in productos_file.readlines():
            valores = producto_line.strip().split(",")
            nombre = valores[0]
            precio = int(valores[1])
            cantidad = int(valores[2])
            inventario.append([nombre, precio, cantidad])
            index_producto.append(nombre)

    # Aqui se leen las acciones
    # Por completar: Hacer las acciones
    with open(acciones_path, "r") as acciones_file:
        for accion_line in acciones_file.readlines():
            valores = accion_line.strip().split(",")
            accion = valores[0]
            rut = valores[1]
            if accion == "Agregar al carro":
                producto = valores[2]
                if producto in index_producto:
                    if (rut not in rut_lista and inventario[index_producto.index(producto)][2] != 0):
                        rut_lista.append([rut, producto])
                        rut_index.append(rut)
                        inventario[index_producto.index(producto)][2] -= 1
                        print(f"[{rut}] {producto} agregado al carro.")
                    elif inventario[index_producto.index(producto)][2] != 0:
                        rut_lista[rut_index(rut)].append(producto)
                        inventario[index_producto.index(producto)][2] -= 1
                        print(f"[{rut}] {producto} agregado al carro.")
                    else:
                        print(f"[{rut}] No quedan unidades de {producto}.")
                else:
                    print(f"[{rut}] No se ha añadido nada al carro, producto invalido")
            elif accion == "Sacar del carro":
                if rut not in rut_index:
                    print(f"[{rut}] El carro esta vacio, no se ha eliminado ningun elemento del carro.")
                elif len(rut_lista[rut_index.index(rut)]) == 1:
                    print(f"[{rut}] El carro esta vacio, no se ha eliminado ningun elemento del carro.")
                else:
                    temporal_producto = rut_lista[rut_index.index(rut)].pop()
                    inventario[index_producto.index(temporal_producto)][2] += 1
                    print(f"[{rut}] Se ha quitado del carro {temporal_producto}")
            elif accion == "Cerrar sesion":
                if rut not in rut_index:
                    print(f"[{rut}] Se ha cerrado la sesion")
                elif len(rut_lista[rut_index.index(rut)]) == 1:
                    print(f"[{rut}] Se ha cerrado la sesion")
                else:
                    for a in rut_lista[rut_index.index(rut)]:
                        rut_lista[rut_index.index(rut)].pop()
                        if a in index_producto:
                            inventario[index_producto.index(a)][2] += 1
                    print(f"[{rut}] Sesion cerrada, se han devuelto los productos del carro.")
            elif accion == "Pagar":
                if rut not in rut_index:
                    print(f"[{rut}] No hay nada que pagar")
                elif len(rut_lista[rut_index.index(rut)]) == 1:
                    print(f"[{rut}] No hay nada que pagar")
                else:
                    contador_precio = 0
                    for i in rut_lista[rut_index.index(rut)]:
                        if i in index_producto: 
                            contador_precio = contador_precio + inventario[index_producto.index(i)][1]
                    print(f"[{rut}] Se pago {contador_precio}.")