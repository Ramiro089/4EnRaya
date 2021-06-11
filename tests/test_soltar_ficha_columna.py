from src.Cuatro_En_Raya import SoltarFichaEnColumna
from src.Cuatro_En_Raya import tableroVacio

def test_soltar_ficha():
	tablero = tableroVacio()
	secuencia = []
	ficha = 1
	columna = 8
	Verificar = SoltarFichaEnColumna(ficha, columna, tablero, secuencia)


	assert secuencia == []
