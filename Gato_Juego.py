from tkinter import *
from tkinter import ttk

def mostrar_tablero():
    for i in range(3):
        for j in range(3):
            botones[i][j].config(text=tablero[i][j])
    if ganador:
        dibujar_linea(ganador_linea)

def comprobar_ganador():
    # Comprobar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0], [(i, 0), (i, 1), (i, 2)]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i], [(0, i), (1, i), (2, i)]
    
    # Comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0], [(0, 0), (1, 1), (2, 2)]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2], [(0, 2), (1, 1), (2, 0)]
    
    return None, []

def realizar_movimiento(fila, col):
    global turno, ganador  # Asegúrate de incluir ganador aquí
    if tablero[fila][col] == " ":
        tablero[fila][col] = jugadores[turno]
        mostrar_tablero()
        ganador, combinacion = comprobar_ganador()
        if ganador:
            mostrar_gato(ganador)
            mensaje.set(f"¡El jugador {ganador} gana!")
            deshabilitar_botones()
            root.after(2000, inicializar_juego)  # Reiniciar después de 2 segundos
            return
        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            mostrar_gato("empate")
            mensaje.set("¡Es un empate!")
            deshabilitar_botones()
            root.after(2000, inicializar_juego)  # Reiniciar después de 2 segundos
            return
        turno = 1 - turno  # Cambia de jugador
        mensaje.set(f"Turno del jugador {jugadores[turno]}")
    else:
        mensaje.set("Movimiento inválido. Inténtalo de nuevo.")

def mostrar_gato(estado):
    canvas.delete("all")  # Limpiar el canvas
    if estado == "X" or estado == "O":
        # Gato feliz
        canvas.create_text(150, 50, text="😺", font=("Arial", 100))
    elif estado == "empate":
        # Gato pensando
        canvas.create_text(150, 50, text="😼", font=("Arial", 100))
    else:
        # Gato triste
        canvas.create_text(150, 50, text="😿", font=("Arial", 100))

def dibujar_linea(combinacion):
    for (i, j) in combinacion:
        botones[i][j].config(bg='yellow')  # Cambiar el color de los botones ganadores
    
    if combinacion:
        x1, y1 = combinacion[0][1] * 100 + 50, combinacion[0][0] * 100 + 50
        x2, y2 = combinacion[2][1] * 100 + 50, combinacion[2][0] * 100 + 50
        canvas.create_line(x1, y1, x2, y2, fill="red", width=5)

def deshabilitar_botones():
    for i in range(3):
        for j in range(3):
            botones[i][j].config(state=DISABLED)

def inicializar_juego():
    global tablero, jugadores, turno, ganador, ganador_linea
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0
    ganador = None  # Inicializar ganador aquí
    ganador_linea = []
    mensaje.set("Turno del jugador X")
    mostrar_tablero()
    for i in range(3):
        for j in range(3):
            botones[i][j].config(state=NORMAL)
    canvas.delete("all")  # Limpiar el canvas al reiniciar

root = Tk()
root.title("Juego del Gato")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mensaje = StringVar()
mensaje_label = ttk.Label(mainframe, textvariable=mensaje)
mensaje_label.grid(column=1, row=0, columnspan=3, sticky=(E, W))

ttk.Label(mainframe, text="Selecciona una posición").grid(column=1, row=1, columnspan=3, sticky=E)

botones = []
for i in range(3):
    fila_botones = []
    for j in range(3):
        btn = ttk.Button(mainframe, text=" ", command=lambda fila=i, col=j: realizar_movimiento(fila, col))
        btn.grid(column=j+1, row=i+2, sticky=W)
        fila_botones.append(btn)
    botones.append(fila_botones)

# Canvas para dibujar gatos y líneas
canvas = Canvas(mainframe, width=300, height=100)
canvas.grid(column=1, row=5, columnspan=3)

inicializar_juego()

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()