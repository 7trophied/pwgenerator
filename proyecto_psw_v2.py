# Generador de contrasenas aleatorias 
""" 
Necesitamos pedir las preferencias del usuario
 - Longitud
 - Puede contener mayusculas
 - Puede contener caracteres especiales
 - Puede contener numeros
""" 
# Tomar todos los caracteres disponibles
# Seleccionar aleatoriamente los caracteres segun la longitud
# Asegurar que se haya seleccionado un caracter de cada tipo (mayusculas, especiales y numeros)
# Asegurar que la longitud es valida

import random
import string               # Nos da acceso a una lista de todos los caracteres incluyendo mayusculas, especiales y numeros.

import tkinter as tk            # Agregamos interfaz grafica
from tkinter import messagebox

def generar_contrasena():
    try:
        longitud = int(entry_longitud.get().strip())     # Solicita longitud deseada
    except ValueError:
        messagebox.showerror("error", "ingresa una longitud valida")
        return

    incluir_mayusculas = var_mayusculas.get()            # Incluir letras mayusculas? (si/no)
    incluir_especiales = var_especiales.get()            # Incluir caracteres especiales? (si/no)
    incluir_numeros = var_numeros.get()                  # Incluir numeros? (si/no)

    if longitud < 4:
        messagebox.showerror("error", "tu longitud tiene que ser mayor a 4")
        return

    minus = string.ascii_lowercase          # Me da todas las letras minusculas
    mayus = string.ascii_uppercase if incluir_mayusculas else "" # -> Cadena vacia               
    especial = string.punctuation if incluir_especiales else ""                         # Operadores Ternarios 
    numeros =  string.digits if incluir_numeros else ""
    todos_caracteres = minus + mayus + especial + numeros                                     

    caracteres_requeridos = []
    if incluir_mayusculas:
        caracteres_requeridos.append(random.choice(mayus))
    if incluir_especiales:
        caracteres_requeridos.append(random.choice(especial))
    if incluir_numeros:
        caracteres_requeridos.append(random.choice(numeros))

    longutud_faltante = longitud - len(caracteres_requeridos)
    contrasena = caracteres_requeridos

    for _ in range(longutud_faltante):                  #el guion bajo holdea el espacio cuando no quieres definir algo
        caracter = random.choice(todos_caracteres)
        contrasena.append(caracter)

    random.shuffle(contrasena)      # Mezcla aun mas la contrasena

    str_contrasena = "".join(contrasena)    #Une todos los elementos usando la cadena sobre la que se llama (cadena vacía) como separador
    entrada_resultado.delete(0, tk.END)
    entrada_resultado.insert(0, str_contrasena)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contrasenas")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Elementos visuales
tk.Label(ventana, text="Ingrese la longitud deseada:").pack(pady=5)
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

var_mayusculas = tk.BooleanVar()
var_especiales = tk.BooleanVar()
var_numeros = tk.BooleanVar()

tk.Checkbutton(ventana, text="Puede contener mayusculas", variable=var_mayusculas).pack(anchor='w', padx=20)
tk.Checkbutton(ventana, text="Puede contener caracteres especiales", variable=var_especiales).pack(anchor='w', padx=20)
tk.Checkbutton(ventana, text="Puede contener numeros", variable=var_numeros).pack(anchor='w', padx=20)

tk.Button(ventana, text="Generar contrasena", command=generar_contrasena).pack(pady=10)

entrada_resultado = tk.Entry(ventana, width=40, font=("Courier", 12))
entrada_resultado.pack(pady=5)

#comprobar inicio
print("iniciado")

# ejecutar interfaz
ventana.mainloop()
