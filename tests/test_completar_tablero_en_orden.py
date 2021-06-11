from src.Cuatro_En_Raya import tableroVacio
from src.Cuatro_En_Raya import completarTableroEnOrden

def test_completar_tablero_orden():
	tablero = tableroVacio()
	secuencia = [1,2,3,1]
	tablero = completarTableroEnOrden(secuencia, tablero)

	assert tablero == [
				[' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[' ', ' ', ' ', ' ', ' ', ' ', ' '],
				[2, ' ', ' ', ' ', ' ', ' ', ' '],
				[1, 2, 1, ' ', ' ', ' ', ' '],
				]
