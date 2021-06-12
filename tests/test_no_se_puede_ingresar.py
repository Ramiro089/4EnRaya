from src.Cuatro_En_Raya import SoltarFichaEnColumna
from src.Cuatro_En_Raya import tableroVacio

def test_completar_tablero_orden():
    tablero =  [
				[2, ' ', ' ', ' ', ' ', ' ', ' '],
				[1, ' ', ' ', ' ', ' ', ' ', ' '],
				[2, ' ', ' ', ' ', ' ', ' ', ' '],
				[1, ' ', ' ', ' ', ' ', ' ', ' '],
				[2, ' ', ' ', ' ', ' ', ' ', ' '],
				[1, ' ', ' ', ' ', ' ', ' ', ' ']
				]
    secuencia = [1,1,1,1,1,1]
    String = SoltarFichaEnColumna(1, 1, tablero, secuencia)

    assert String == print ("No hay espacios en esa columna, ingrese otra")
