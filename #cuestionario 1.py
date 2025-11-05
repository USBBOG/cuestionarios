#cuestionario 
import tkinter as tk
from tkinter import messagebox


preguntas = [
    {
        "pregunta": "1. ¿Qué es una tupla en Python?",
        "opciones": [
            "a) Una lista que se puede modificar",
            "b) Una colección ordenada e inmutable de elementos",
            "c) Un conjunto de datos sin orden"
        ]
    },
    {
        "pregunta": "2. ¿Cuál de las siguientes opciones crea una tupla correctamente?",
        "opciones": [
            "a) tupla = [1, 2, 3]",
            "b) tupla = (1, 2, 3)",
            "c) tupla = {1, 2, 3}"
        ]
    },
    {
        "pregunta": "3. ¿Qué instrucción se usa para manejar excepciones en Python?",
        "opciones": [
            "a) try - except",
            "b) catch - throw",
            "c) handle - error"
        ]
    },
    {
        "pregunta": "4. ¿Qué hace el bucle 'while'?",
        "opciones": [
            "a) Repite un bloque hasta que se cumpla una condición",
            "b) Repite un bloque un número fijo de veces",
            "c) Ejecuta una sola vez una instrucción"
        ]
    }
]

# Respuestas correctas (no se muestran en la interfaz)
respuestas_correctas = ["b", "b", "a", "a"]

# Ventana principal
root = tk.Tk()
root.title("Cuestionario de Python - Tkinter")
root.geometry("600x400")
root.resizable(False, False)

# Variables globales
indice = 0
puntaje = 0
respuesta_usuario = tk.StringVar()

# Mostrar pregunta
def mostrar_pregunta():
    global indice
    if indice < len(preguntas):
        pregunta_actual = preguntas[indice]
        pregunta_label.config(text=pregunta_actual["pregunta"])
        respuesta_usuario.set(None)
        for i, opcion in enumerate(pregunta_actual["opciones"]):
            botones_opciones[i].config(text=opcion, value=opcion[0])
    else:
        mostrar_resultado()

# Verificar respuesta
def verificar_respuesta():
    global indice, puntaje
    seleccion = respuesta_usuario.get()
    if seleccion == respuestas_correctas[indice]:
        puntaje += 1
    indice += 1
    mostrar_pregunta()

# Mostrar resultado
def mostrar_resultado():
    messagebox.showinfo("Resultado", f"Tu puntaje final es: {puntaje} / {len(preguntas)}")
    root.destroy()

# Interfaz
pregunta_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500, justify="left")
pregunta_label.pack(pady=20)

botones_opciones = []
for _ in range(3):
    boton = tk.Radiobutton(root, text="", variable=respuesta_usuario, font=("Arial", 12))
    boton.pack(anchor="w", padx=40)
    botones_opciones.append(boton)

# Botón siguiente 
boton_siguiente = tk.Button(root, text="Siguiente", command=verificar_respuesta, font=("Arial", 12))
boton_siguiente.pack(pady=20)

# Iniciar con la primera pregunta
mostrar_pregunta()

# Ejecutar la app
root.mainloop()
