import tkinter as tk

def convertir():
    try: 
        kilometros = float(entrada_kilometros.get())
        millas = kilometros * 0.621371
        etiqueta_resultado.config(text=f"{kilometros} kilometros son {millas} millas")
        
    except ValueError:
        etiqueta_resultado.config(text="Ingrese un numero numerico valido")  
    
ventana = tk.Tk()
ventana.title("Conversor de Kilometros a Millas")
ventana.geometry("300x150")
    
etiqueta_instruccion =tk.Label(ventana, text="Ingrese la distancia en Kilometros")
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    
entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0,padx=10, pady=10)
    
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir )
boton_convertir.grid(row=1, column=1, padx=10, pady=10)
    
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=0, pady=10)
    
ventana.mainloop()   