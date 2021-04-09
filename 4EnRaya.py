import os
import sys

def tableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def SoltarFichaEnColumna(ficha, columna, tablero, secuncia):
    for fila in range(6, 0, -1):
        if columna > 7:
            os.system('cls')
            print ("Ingrese un numero entre 1-6")
            return 
        elif tablero [fila - 1][columna - 1] == 0:
            secuncia[len(secuencia):] = [columna]
            #secuencia.append([columna])
            os.system('cls')
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
    return tablero

def dibujarTablero(tablero):
    n=0
    while n<6:
     print (tablero[n][0],tablero[n][1],tablero[n][2],tablero[n][3],tablero[n][4],tablero[n][5],tablero[n][6])  
     n += 1
    return tablero

def ganador(tablero):
    i=5
    while i >= 0:
        j=0
        while j <= 3:
            if tablero[i][j] != 0 and tablero[i][j] == tablero[i][j+1] and tablero[i][j] == tablero[i][j+2] and tablero[i][j] == tablero[i][j+3]:
                print("Gano el Jugador " + str(tablero[i][j])) 
                sys.exit()
            else:
                j += 1
        i -= 1
    i=0
    while i <= 6:
        j=5
        while j >= 3:
            if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i] and tablero[j][i] == tablero[j-2][i] and tablero[j][i] == tablero[j-3][i]:
                print("Gano el Jugador " + str(tablero[j][i])) 
                sys.exit()
            else:
                j -= 1
        i += 1
    diagonal(tablero)

def diagonal(tablero):
    r=0
    j=0
    while r <=6 :
        if r==0:
           i=r
           j=5
           while j >= 3:
                if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i+1] and tablero[j][i] == tablero[j-2][i+2] and tablero[j][i] == tablero[j-3][i+3]:
                    print("Gano el Jugador " + str(tablero[j][i])) 
                    sys.exit()
                else:
                    j -= 1
                    i += 1
        elif r==1:
            i=r
            j=5
            while j >= 3:
                if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i+1] and tablero[j][i] == tablero[j-2][i+2] and tablero[j][i] == tablero[j-3][i+3]:
                    print("Gano el Jugador " + str(tablero[j][i])) 
                    sys.exit()
                else:
                    j -= 1
                    i += 1
        elif r==2:
            i=r
            j=5
            while j >= 4:
                if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i+1] and tablero[j][i] == tablero[j-2][i+2] and tablero[j][i] == tablero[j-3][i+3]:
                    print("Gano el Jugador " + str(tablero[j][i])) 
                    sys.exit()
                else:
                    j -= 1
                    i += 1
        elif r==3:
            i=r
            j=5
            if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i+1] and tablero[j][i] == tablero[j-2][i+2] and tablero[j][i] == tablero[j-3][i+3]:
                print("Gano el Jugador " + str(tablero[j][i])) 
                sys.exit()
            elif tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i-1] and tablero[j][i] == tablero[j-2][i-2] and tablero[j][i] == tablero[j-3][i-3]:
              print("Gano el Jugador " + str(tablero[j][i])) 
              sys.exit()
        elif r==4:
            i=r
            j=5
            while j >= 4:
                if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i-1] and tablero[j][i] == tablero[j-2][i-2] and tablero[j][i] == tablero[j-3][i-3]:
                    print("Gano el Jugador " + str(tablero[j][i])) 
                    sys.exit()
                else:
                    j -= 1
                    i += 1
        elif r==5:
            i=r
            j=5
            while j >= 3:
                if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i-1] and tablero[j][i] == tablero[j-2][i-2] and tablero[j][i] == tablero[j-3][i-3]:
                    print("Gano el Jugador " + str(tablero[j][i])) 
                    sys.exit()
                else:
                    j -= 1
                    i -= 1
        elif r==6:
            i=r
            j=5
            while j >= 3:
                if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i-1] and tablero[j][i] == tablero[j-2][i-2] and tablero[j][i] == tablero[j-3][i-3]:
                    print("Gano el Jugador " + str(tablero[j][i])) 
                    sys.exit()
                else:
                    j -= 1
                    i -= 1
        r += 1
    j=0
    i=3
    if tablero[j][i] != 0 and tablero[j][i] == tablero[j+1][i+1] and tablero[j][i] == tablero[j+2][i+2] and tablero[j][i] == tablero[j+3][i+3]:
        print("Gano el Jugador " + str(tablero[j][i])) 
        sys.exit()
    elif tablero[j][i] != 0 and tablero[j][i] == tablero[j+1][i-1] and tablero[j][i] == tablero[j+2][i-2] and tablero[j][i] == tablero[j+3][i-3]:
        print("Gano el Jugador " + str(tablero[j][i])) 
        sys.exit()
    j=4
    i=0
    while j >= 3:
        print(i)
        if tablero[j][i] != 0 and tablero[j][i] == tablero[j-1][i+1] and tablero[j][i] == tablero[j-2][i+2] and tablero[j][i] == tablero[j3][i+3]:
            print("Gano el Jugador " + str(tablero[j][i])) 
            sys.exit()
        else:
            i += 1
            j -= 1
    j=4
    i=6
    while j >= 3:
        if tablero[j][i] != 0 and tablero[j][i] == tablero[j+1][i-1] and tablero[j][i] == tablero[j+2][i-2] and tablero[j][i] == tablero[j+3][i-3]:
            print("Gano el Jugador " + str(tablero[j][i])) 
            sys.exit()
        else:
            i -= 1
            j -= 1
    
        

tablero = tableroVacio()
secuencia = []
c=0
f=0
os.system('cls')
#dibujarTablero (tablero)
while 1 > 0:
    c = int(input("Ingrese columna: "))
    if len(secuencia)%2 == 0:
        f=1
    else:
        f=2
    SoltarFichaEnColumna(f,c,tablero,secuencia)
    os.system('cls')
    tablero = dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))
    ganador(tablero)
