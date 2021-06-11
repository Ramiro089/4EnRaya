from src.Cuatro_En_Raya import tableroVacio
from src.Cuatro_En_Raya import ganador
from src.Cuatro_En_Raya import diagonal

def test_ganador():
        secuencia = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

        String = ganador(secuencia)

        assert String == 0
