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

def generar_contrasena():
    longitud = int(input ("Ingrese la longitud deseada: ").strip())
    incluir_mayusculas = input ("Incluir letras mayusculas? (si/no):").strip().lower()
    incluir_especiales = input ("Incluir caracteres especiales? (si/no):").strip().lower()
    incluir_numeros = input ("Incluir numeros? (si/no):").strip().lower()

    if longitud < 4:
        print("La longitud de la contrasena tiene que ser de por lo menos 4 caracetres.")
        return
        
    minus = string.ascii_lowercase          # Me da todas las letras minusculas
    mayus = string.ascii_uppercase if incluir_mayusculas == "si" else "" # -> Cadena vacia               
    especial = string.punctuation if incluir_especiales == "si" else ""                         # Operadores Ternarios 
    numeros =  string.digits if incluir_numeros == "si" else ""
    todos_caracteres = minus + mayus + especial + numeros                                     

    caracteres_requeridos = []
    if incluir_mayusculas == "si" :
        caracteres_requeridos.append(random.choice(mayus))
    if incluir_especiales == "si" :
        caracteres_requeridos.append(random.choice(especial))
    if incluir_numeros == "si" :
        caracteres_requeridos.append(random.choice(numeros))

    longutud_faltante = longitud - len(caracteres_requeridos)
    contrasena = caracteres_requeridos

    for _ in range(longutud_faltante):                  #el guion bajo holdea el espacio cuando no quieres definir algo
        caracter = random.choice(todos_caracteres)
        contrasena.append(caracter)

    random.shuffle(contrasena)      # Mezcla aun mas la contrasena

    str_contrasena = "".join(contrasena)    #Une todos los elementos usando la cadena sobre la que se llama (cadena vacía) como separador
    return str_contrasena

contrasena = generar_contrasena()
print(contrasena)
