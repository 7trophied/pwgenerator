Update 1:
# Generador de Contraseñas Aleatorias

Este es un programa basico en python que genera contraseñas seguras y aleatorias según las preferencias del usuario.  
Permitiendo configurar su longitud, elegir si incluir letras mayúsculas, caracteres especiales y números.

## Características

- Permite personalizar segun estos aspectos:
  
  - Longitud de la contraseña
  - Inclusión de letras mayúsculas
  - Inclusión de caracteres especiales (símbolos como `!@#$%`)
  - Inclusión de números
- Asegura que se incluya al menos un carácter de cada tipo seleccionado
- Mezcla aleatoriamente los caracteres para mayor seguridad

## Requisitos

- Python 3.x
- Librerías:
  - `random`
  - `string`

#### No requiere instalación especial. Solo descarga el archivo `.py` y ejecútalo con Python.

```bash
python generador_contrasena.py
```

Update 2:

# Generador de Contraseñas Aleatorias (v2.0)
Este programa en Python genera contraseñas seguras y aleatorias según las preferencias del usuario, ahora con una interfaz gráfica (GUI) más facil y amigable.

 Novedades en la Versión 2
- Interfaz gráfica con Tkinter
- Validación de entrada mejorada
- Diseño más intuitivo con checkboxes para opciones
- Visualización clara de la contraseña generada
- Mensajes de error descriptivos

## Características principales
- Personalización completa:
  
    - Longitud de la contraseña (mínimo 4 caracteres)
    - Inclusión de letras mayúsculas
    - Inclusión de caracteres especiales
    - Inclusión de números

- Garantiza que se incluya al menos un carácter de cada tipo seleccionado

- Mezcla aleatoria avanzada para máxima seguridad

- Interfaz limpia, sencilla y fácil de usar

## Requisitos
- Python 3.x
- Librerías:
  - `random`
  - `string`
  - `tkinter`


## Instrucciones de uso

1. Ejecuta el programa:

```bash
python generador_contrasena_v2.py
```

2. Completa los campos en la interfaz:
  - Ingresa la longitud deseada (mínimo 4)
  - Selecciona los tipos de caracteres a incluir
  - Haz clic en "Generar contraseña"
  - Copia tu contraseña segura desde el campo de resultado
