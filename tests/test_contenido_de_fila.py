from src.Cuatro_En_Raya import tableroVacio
from src.Cuatro_En_Raya import contenidoFila

def test_contenido_columna():
        tablero = [
        [' ', 1 , ' ', ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
    ]
        verificar=contenidoFila(1, tablero)

        assert verificar == [' ', 1, ' ', ' ', ' ', ' ', ' ']
