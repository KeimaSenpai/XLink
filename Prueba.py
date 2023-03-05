import urllib.request
import tkinter as tk
import tkinter.filedialog as fd


def download_file():
    url = url_entry.get()
    save_path = fd.asksaveasfilename()
    urllib.request.urlretrieve(url, save_path)


# Crear la ventana principal
window = tk.Tk()

# Crear un lienzo para colocar los widgets
canvas = tk.Canvas(window, height=200, width=300)
canvas.pack()

# Crear la etiqueta y el cuadro de entrada para la URL
url_label = tk.Label(canvas, text="URL:")
url_label.place(relx=0.1, rely=0.1)
url_entry = tk.Entry(canvas)
url_entry.place(relx=0.3, rely=0.1)

# Crear el botón de descarga y asignar a la función download_file
download_button = tk.Button(canvas, text="Descargar", command=download_file)
download_button.place(relx=0.4, rely=0.4)

window.mainloop()
