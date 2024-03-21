# Lina Yulieth Ballesteros 
# Fredy Jeanpier Rodriguez 

#Proyecto sobre un supermercado, calcula la lista de productos, forma de pago 

import tkinter as tk

#Funcion para agregar un producto a la lista
def agregar_producto():
    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    pago = metodo_pago.get()
    producto = f"Nombre: {nombre}, Precio: {precio}, Pago: {pago}"
    lista_productos.insert(tk.END, producto)
    
#Funcion para pedir los datos de la lista 

def ingresar_producto(item):
    # Se crear un arreglo 
    partes = item.split(", ")
    nombre = partes[0].split(": ")[1]
    precio = partes[1].split(": ")[1]
    pago = partes[2].split(": ")[1]
    return nombre, precio, pago

ventana = tk.Tk() #Contenedor de graficos
ventana.geometry("400x400")
ventana.title("Supermercado El solecito")

#Con el uso del frame se ubican los nombres de las cajs de texto
frame_datos = tk.Frame(ventana)
frame_datos.place(x=20,y=20)

# Etiqueta para nombre del producto
label_nombre = tk.Label(frame_datos, text="Producto:")
#Posicion de la etiqueta, a la izquierda de la ventana
label_nombre.grid(row=0, column=0)
#Estructura de la caja de texto
entry_nombre = tk.Entry(frame_datos)
#Posicion de la caja de texto
entry_nombre.grid(row=0, column=1)

#Se usa la misma estructura de arriba 
label_precio = tk.Label(frame_datos, text="Precio:")
label_precio.grid(row=1, column=0)
entry_precio = tk.Entry(frame_datos)
entry_precio.grid(row=1, column=1)

#Con el uso de un pack se posicionan los datos
frame_datos.pack()
frame_pago = tk.Frame(ventana)
frame_pago.place(x=20, y=70)

# 
metodo_pago = tk.StringVar(value="Contado")
label_pago = tk.Label(frame_pago, text="Método de pago:")
label_pago.pack()

radio_contado = tk.Radiobutton(
    frame_pago, text="Contado", variable=metodo_pago, value="Contado")
radio_contado.pack()

radio_credito = tk.Radiobutton(
    frame_pago, text="Crédito", variable=metodo_pago, value="Crédito")
radio_credito.pack()
frame_pago.pack()


frame_botones = tk.Frame(ventana)
frame_botones.place(x=20, y=130)

boton_agregar = tk.Button(
    frame_botones, text="Agregar", command=agregar_producto)
boton_agregar.pack()

frame_botones.pack()

frame_lista = tk.Frame(ventana)
frame_lista.place(x=20, y=220)

lista_productos = tk.Listbox(frame_lista, width=50, height=10)
lista_productos .pack()
frame_lista.pack()
ventana.mainloop()




