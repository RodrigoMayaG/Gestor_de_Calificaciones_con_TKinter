
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

url = r"C:\Users\rodri\OneDrive\Documentos\PYTHON\registro_resultados\registro.csv"
root = tk.Tk()
root.config(bg= "lightgray")
root.title('Gestor de calificacion')
registro = pd.read_csv(url)


def carga ():
    for widgets in root.winfo_children():
        widgets.destroy()
    
    mensaje_1_carga = tk.Label(root, text="Bienvenido al menú de carga de información\n\n", font=("Arial",20), bg="green", fg="white", relief=tk.RAISED)
    mensaje_2_carga = tk.Label(root, text="\nIngresa los datos solicitados: ",anchor="center", bd=3, font=("Arial", 15),bg= "lightgray")
    mensaje_1_carga.pack(anchor="center")
    mensaje_2_carga.pack()


    frame = tk.Frame(root, bg="lightgray")
    frame.pack(pady=20)

    label_1 = tk.Label(frame, text="Nombre", bg="lightgray")
    label_1.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry = tk.Entry(frame)
    entry.grid(row=0, column=1, padx=5, pady=5)
    label_2 = tk.Label(frame, text="Calificación", bg="lightgray")
    label_2.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_2 = tk.Entry(frame)
    entry_2.grid(row=1, column=1, padx=5, pady=5)
    label_3 = tk.Label(frame, text= "Materia", bg= "lightgray")
    label_3.grid(row=2, column=0, padx=5, pady=5)
    entry_3 = tk.Entry(frame)
    entry_3.grid(row=2, column=1, padx=5, pady= 5)

    def guardar ():
        global registro
        data_nombre = entry.get()
        data_califi = entry_2.get()
        data_materia = entry_3.get()
        diccionario = {"Nombre": data_nombre,
                       "Calificacion": data_califi,
                       "Materia": data_materia}
        mini_df = pd.DataFrame([diccionario])
        registro = pd.concat([registro, mini_df], ignore_index=True)
        registro.to_csv(url, index=False)
        entry.delete(0,tk.END)
        entry_2.delete(0,tk.END)
        entry_3.delete(0,tk.END)
        

    boton_guardar = tk.Button(frame,command=guardar, text= "Guardar", activebackground="blue", activeforeground="white", width=30)
    boton_guardar.grid(row=8, column=1)
    boton_regresar = tk.Button(frame,command= menu_principal, text= "Regresar",activebackground="blue", activeforeground="white", width=30)
    boton_regresar.grid(column=1)



def analisis():
    for widgets in root.winfo_children():
        widgets.destroy()
    
    
    mensaje_ana_1 = tk.Message(root, text= "Bienvenido al analisis de la información\n\n",font=("Arial",20), bg="green", fg="white", relief=tk.RAISED, width= 1000)
    mensaje_ana_1.grid(row=0, column=1)

    df = pd.read_csv(url)
    materia_group =df.groupby('Materia')["Calificacion"].mean().sort_values(ascending=False)

    fig_1 = Figure(figsize=(4,4))
    ax1 = fig_1.add_subplot(111)
    bars = ax1.bar(materia_group.index, materia_group.values)
    ax1.set_xticklabels(materia_group.index, fontsize=7, rotation = 20)
    ax1.set_title('Promedio de calificación por materia')
    for bar in bars:
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{int(bar.get_height())}', 
                 ha='center', va='bottom', fontsize=7)
        
    alumnos = df.groupby('Materia')['Nombre'].count()
    fig_2 = Figure(figsize=(4,4))
    ax2= fig_2.add_subplot(111)
    bars2 =ax2.bar(alumnos.index, alumnos.values)
    ax2.set_xticklabels(alumnos.index, fontsize=7, rotation=20)
    ax2.set_title('Materias con el mayor numero de alumnos')
    for bar in bars2:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{int(bar.get_height())}', 
                 ha='center', va='bottom', fontsize= 7)
        
    
    calificaciones = df['Calificacion']

    fig_3 = Figure(figsize=(4,4))
    ax3 = fig_3.add_subplot(111)
    histograma = ax3.hist(calificaciones, bins=range(int(calificaciones.min()), int(calificaciones.max())+2), edgecolor='black', align='left')
    ax3.set_xticks(range(int(calificaciones.min()), int(calificaciones.max())+1))
    ax3.set_xlabel('Calificación')
    ax3.set_ylabel('Número de alumnos')
    ax3.set_title('Distribución de calificaciones')

    canvas_1 = FigureCanvasTkAgg(fig_1, master= root)
    canvas_1.draw()
    canvas_1.get_tk_widget().grid(row=3, column=0)

    canvas_2 = FigureCanvasTkAgg(fig_2, master= root)
    canvas_2.draw()
    canvas_2.get_tk_widget().grid(row=3, column=1)

    canvas_3 = FigureCanvasTkAgg(fig_3, master= root)
    canvas_3.draw()
    canvas_3.get_tk_widget().grid(row=3, column=2)

    boton_regresar = tk.Button(root,command= menu_principal, text= "Regresar",activebackground="blue", activeforeground="white", width=30)
    boton_regresar.grid(row=5, column= 1)


def menu_principal():

    for widgets in root.winfo_children():
        widgets.destroy()

    def cerrar():
        root.destroy()

    mensaje_1 = tk.Label(root,text="Bienvenido al gestor de calificaciones", font=("Arial",20), bg="green", fg="white",relief=tk.RAISED)
    mensaje_2 = tk.Label(root, text= "\n\nIngresa la opcion requerida:\n\n", anchor="center", bd=3, font=("Arial", 15),bg= "lightgray")
    boton_llenar = tk.Button(root, command= carga, text="Carga de informacion",activebackground="blue", activeforeground="white", width=30)
    boton_analizar = tk.Button(root, command= analisis, text="Analizar data", activebackground="blue", activeforeground="white", width=30)
    boton_salir = tk.Button(root, command=cerrar, text="Salir", activebackground="blue", activeforeground="white", width=30)
    mensaje_3 = tk.Label(root,text="\nInstrucciones", font=("Arial",15), fg="black",bg= "lightgray")
    comentario_1 = tk.Label(root, text="\nCarga de info: Agregar nombre del alumno, calificaciones y materia",bg= "lightgray")
    comentario_2 = tk.Label(root, text="\nExtraer CSV: Descargar información en formato excel",bg= "lightgray")
    comentario_3 = tk.Label(root, text="\nAnalizar data: Genera un analisis de las calificaciones para tener una visualizacion general\n\n",bg= "lightgray")
    mensaje_1.pack(anchor="center")
    mensaje_2.pack()
    boton_llenar.pack()
    boton_analizar.pack()
    boton_salir.pack()
    mensaje_3.pack()
    comentario_1.pack(anchor="s",)
    comentario_2.pack(anchor="s")
    comentario_3.pack(anchor="s")
    root.mainloop()

menu_principal() 
