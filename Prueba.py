# Lina Yulieth Ballesteros 
# Fredy Jeanpier Rodriguez 

#Proyecto sobre un supermercado, calcula la lista de productos, forma de pago 

import tkinter as tk

#Primero Colocamos las funciones 

#Funcion para agregar un producto a la lista
def agregar_producto():
    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    pago = metodo_pago.get()
    
#Funcion para pedir los datos de la lista  
def ingresar_producto():
    nombre = str(cajaNumero1.get())
    precio = str(cajaNumero2.get())
    pago = str(cajaNumero3.get())
    return nombre, precio, pago

#Definimos la ventana, titulo y tamaño
ventana = tk.Tk() 
ventana.geometry("400x400")
ventana.title("Supermercado El solecito")

#Definimos las cajas de texto
cajaNumero1 = tk.Entry(ventana,font="Helveltica 20 ") #Caja para ingresar datos 
cajaNumero1.place(x=10,y=50)

cajaNumero2 = tk.Entry(ventana,font="Herlveltica 20") 
cajaNumero2.pack()
cajaNumero3 = tk.Entry(ventana,font="Herlveltica 20") 
cajaNumero3.pack()




frame_datos = tk.Frame(ventana)
frame_datos.place(x=20,y=20)

# Posicionar el producto 
label_nombre = tk.Label(frame_datos, text="Prodcuto:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(frame_datos)
entry_nombre.grid(row=0, column=1)

#Posicionar el precio
label_precio = tk.Label(frame_datos, text="Precio:")
label_precio.grid(row=1, column=0)
entry_precio = tk.Entry(frame_datos)
entry_precio.grid(row=1, column=1)
frame_datos.pack()

frame_pago = tk.Frame(ventana)
frame_pago.place(x=20, y=70)

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

lista_animales = tk.Listbox(frame_lista, width=50, height=10)
lista_animales.pack()
frame_lista.pack()
ventana.mainloop()




