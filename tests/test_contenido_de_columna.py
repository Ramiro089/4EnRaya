from src.Cuatro_En_Raya import tableroVacio
from src.Cuatro_En_Raya import contenidoColumna

def test_contenido_fila():
	tablero = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
    ]
	verificar=contenidoColumna(1, tablero)

	assert verificar == [' ', ' ',1,1,1,1]
