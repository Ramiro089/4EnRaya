from src.Cuatro_En_Raya import tableroVacio
from src.Cuatro_En_Raya import ganador

def test_ganador():
	secuencia = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
    ]
	secuencia1 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [1, 1, 1, 1, ' ', ' ', ' '],
    ]

	String = ganador(secuencia)
	String1 = ganador(secuencia1)


	assert String == 0
	assert String1 == 0
