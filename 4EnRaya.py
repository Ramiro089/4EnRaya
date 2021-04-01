def tableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def SoltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero [fila - 1][columna - 1] == 0:
            tablero [fila - 1][columna - 1 ] == ficha
            return


def completarTableroEnOrden(secuencia, tablero):
    n=0
    o=0
    i=0
    while n < len(secuencia):
        if tablero [5-o][secuencia[n]-1] == 0:
            if n%2 == 0:
             tablero [5-o][secuencia[n]-1] = 1
            elif n%2 != 0:
                tablero [5-o][secuencia[n]-1] = 2
        elif tablero [5-o][secuencia[n]-1] == 1 or tablero [5-o][secuencia[n]-1] == 2:
          i=o
          while i < len(secuencia):
            if tablero [6-i-1][secuencia[n]-1] == 1 or tablero [6-i-1][secuencia[n]-1] == 2:
              i += 1
            else:
                if n%2 == 0:
                    tablero [6-i-1][secuencia[n]-1] = 1
                    i=len(secuencia)
                else:
                    tablero [6-i-1][secuencia[n]-1] = 2
                    i=len(secuencia)
        n += 1
    

def dibujarTablero(tablero):
    n=0
    while n<6:
     print (tablero[n][0],tablero[n][1],tablero[n][2],tablero[n][3],tablero[n][4],tablero[n][5],tablero[n][6])  
     n += 1

tablero = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

secuencia = [1, 2, 3, 1]
completarTableroEnOrden(secuencia, tablero)
dibujarTablero(tablero)