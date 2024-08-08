import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import csv
import os

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        edad = int(entry_edad.get())
        sexo = var_sexo.get()
        nombre = entry_nombre.get()

        if not nombre:
            messagebox.showerror("Error", "Por favor ingrese el nombre del paciente.")
            return

        ks = 1.0 if sexo == "Hombre" else 1.1
        ka = 1 + 0.01 * (edad - 25)
        imc = (peso / (altura ** 2)) * ks * ka

        label_resultado.config(text=f"IMC: {imc:.2f}")

        # Mensajes según el rango de IMC
        if imc < 18.5:
            messagebox.showinfo("Estado de IMC", "IMC indica desnutrición.")
        elif imc >= 18.5 and imc < 24.9:
            messagebox.showinfo("Estado de IMC", "IMC en rango saludable.")
        elif imc >= 24.9 and imc < 29.9:
            messagebox.showinfo("Estado de IMC", "IMC indica sobrepeso.")
        else:
            messagebox.showinfo("Estado de IMC", "IMC indica obesidad.")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

def guardar_datos():
    nombre = entry_nombre.get()
    if not nombre:
        messagebox.showerror("Error", "Por favor ingrese el nombre del paciente.")
        return

    datos = {
        "Nombre": entry_nombre.get(),
        "Peso (kg)": entry_peso.get(),
        "Altura (m)": entry_altura.get(),
        "Edad": entry_edad.get(),
        "Sexo": var_sexo.get(),
        "IMC": label_resultado.cget("text").split(": ")[1]
    }

    archivo = f"{nombre}.csv"
    archivo_existe = os.path.isfile(archivo)

    with open(archivo, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=datos.keys())
        if not archivo_existe:
            writer.writeheader()
        writer.writerow(datos)

    messagebox.showinfo("Guardado", f"Datos guardados en el archivo {archivo}")

# Función para configurar el cursor como hand2 cuando el ratón entra en un botón
def configurar_cursor_hand2(event):
    event.widget.config(cursor="hand2")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Crear un canvas con la imagen de fondo
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Título "IMSS" centrado
titulo_imss = tk.Label(canvas, text="IMSS", font=("Helvetica", 24, "bold"), fg="green")
titulo_imss.place(relx=0.5, y=20, anchor=tk.CENTER)

imagen_fondo = ImageTk.PhotoImage(Image.open("IMSS-logo.png"))
canvas.create_image(0, 0, anchor=tk.NW, image=imagen_fondo)

# Variables
var_sexo = tk.StringVar(value="Hombre")

# Estilo para los botones redondeados
estilo = ttk.Style()
estilo.configure('BotonRedondo.TButton', borderwidth=5, bordercolor="#2CBF4E", background="#6ED185",
                 foreground="black", padx=30, pady=30, relief=tk.RAISED,
                 font=("Helvetica", 12, "bold"))

# Widgets sobre el canvas
tk.Label(canvas, text="Nombre:", font=("Helvetica", 12), justify=tk.CENTER, foreground="green").place(x=50, y=80)
entry_nombre = tk.Entry(canvas, width=25, font=("Helvetica", 12))  # Ajuste en el ancho del Entry
entry_nombre.place(x=200, y=80)

tk.Label(canvas, text="Peso (kg):", font=("Helvetica", 12), justify=tk.CENTER, foreground="green").place(x=50, y=130)
entry_peso = tk.Entry(canvas, width=15, font=("Helvetica", 12))  # Ajuste en el ancho del Entry
entry_peso.place(x=200, y=130)

tk.Label(canvas, text="Altura (m):", font=("Helvetica", 12), justify=tk.CENTER, foreground="green").place(x=50, y=180)
entry_altura = tk.Entry(canvas, width=15, font=("Helvetica", 12))  # Ajuste en el ancho del Entry
entry_altura.place(x=200, y=180)

tk.Label(canvas, text="Edad:", font=("Helvetica", 12), justify=tk.CENTER, foreground="green").place(x=50, y=230)
entry_edad = tk.Entry(canvas, width=15, font=("Helvetica", 12))  # Ajuste en el ancho del Entry
entry_edad.place(x=200, y=230)

tk.Label(canvas, text="Sexo:", font=("Helvetica", 12), justify=tk.CENTER, foreground="green").place(x=50, y=280)
tk.Radiobutton(canvas, text="Hombre", variable=var_sexo, value="Hombre", font=("Helvetica", 10)).place(x=200, y=280)
tk.Radiobutton(canvas, text="Mujer", variable=var_sexo, value="Mujer", font=("Helvetica", 10)).place(x=270, y=280)

# Cargar la imagen para el botón de calcular IMC
image_calcular_imc = Image.open("imss_bot.jpeg")
image_calcular_imc = image_calcular_imc.resize((110, 23), Image.LANCZOS)
image_calcular_imc = ImageTk.PhotoImage(image_calcular_imc)

# Crear el botón con la imagen y configurar el cursor hand2
btn_calcular_imc = ttk.Button(canvas, text="Calcular IMC", image=image_calcular_imc, style='BotonRedondo.TButton', command=calcular_imc, compound=tk.LEFT)
btn_calcular_imc.place(x=50, y=330)
btn_calcular_imc.bind("<Enter>", configurar_cursor_hand2)
btn_calcular_imc.bind("<Leave>", lambda e: btn_calcular_imc.config(cursor=""))

# Crear el botón "Guardar Datos" y configurar el cursor hand2
btn_guardar_datos = ttk.Button(canvas, text="Guardar Datos", style='BotonRedondo.TButton', command=guardar_datos)
btn_guardar_datos.place(x=300, y=330)
btn_guardar_datos.bind("<Enter>", configurar_cursor_hand2)
btn_guardar_datos.bind("<Leave>", lambda e: btn_guardar_datos.config(cursor=""))

label_resultado = tk.Label(canvas, text="IMC: ", font=("Arial", 12), justify=tk.CENTER, foreground="green")
label_resultado.place(x=50, y=380)

# Ejecutar la aplicación
root.mainloop()
