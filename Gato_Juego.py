from tkinter import * # Importa todos los componentes de tkinder
from tkinter import ttk # Importa los componentes mejorado de tkinder

class JuegoGato:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.jugadores = ["X", "O"]
        self.turno = 0
        self.ganador = None

    def comprobar_ganador(self):
        combinaciones = [ [(i, j) for j in range(3)] for i in range(3) ] + \
                         [ [(j, i) for j in range(3)] for i in range(3) ] + \
                         [ [(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)] ]

        for combinacion in combinaciones:
            valores = [self.tablero[i][j] for i, j in combinacion]
            if valores[0] != " " and all(v == valores[0] for v in valores):
                return valores[0], combinacion
        return None, []

    def realizar_movimiento(self, fila, col):
        if self.tablero[fila][col] == " ":
            self.tablero[fila][col] = self.jugadores[self.turno]
            return True
        return False

    def reiniciar_juego(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.turno = 0
        self.ganador = None

def actualizar_tablero():
    for i in range(3):
        for j in range(3):
            botones[i][j].config(text=juego.tablero[i][j])
    if juego.ganador:
        resaltar_ganador(juego.ganador)

def mover(fila, col):
    if juego.realizar_movimiento(fila, col):
        ganador, combinacion = juego.comprobar_ganador()
        if ganador:
            juego.ganador = ganador
            mensaje.set(f"¡El jugador {ganador} gana!")
            deshabilitar_botones()
            root.after(2000, reiniciar)
        elif all(juego.tablero[i][j] != " " for i in range(3) for j in range(3)):
            mensaje.set("¡Es un empate!")
            deshabilitar_botones()
            root.after(2000, reiniciar)
        else:
            juego.turno = 1 - juego.turno
            mensaje.set(f"Turno del jugador {juego.jugadores[juego.turno]}")
        actualizar_tablero()

def resaltar_ganador(combinacion):
    for (i, j) in combinacion:
        botones[i][j].config(bg='yellow')

def deshabilitar_botones():
    for fila in botones:
        for boton in fila:
            boton.config(state=DISABLED)

def reiniciar():
    juego.reiniciar_juego()
    mensaje.set("Turno del jugador X")
    actualizar_tablero()
    for fila in botones:
        for boton in fila:
            boton.config(state=NORMAL)

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
juego = JuegoGato()

for i in range(3):
    fila_botones = []
    for j in range(3):
        btn = ttk.Button(mainframe, text=" ", command=lambda fila=i, col=j: mover(fila, col))
        btn.grid(column=j+1, row=i+2, sticky=W)
        fila_botones.append(btn)
    botones.append(fila_botones)

reiniciar()

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()