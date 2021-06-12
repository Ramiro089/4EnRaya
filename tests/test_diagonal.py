from src.Cuatro_En_Raya import tableroVacio
from src.Cuatro_En_Raya import ganador
from src.Cuatro_En_Raya import diagonal
from src.Cuatro_En_Raya import empate

def test_ganador():
    secuencia0 = [
        [1,2,1,2,1,1],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    String0 = empate(secuencia0)

    secuencia = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    String = ganador(secuencia)

    secuencia1 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
    ]
    String1 = ganador(secuencia1)

    secuencia2 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 1, ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
    ]
    String2 = ganador(secuencia2)

    secuencia3 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', 1],
        [' ', ' ', ' ', ' ', ' ', 1, ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
    ]
    String3 = ganador(secuencia3)

    secuencia3_5 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
    ]
    String3_5 = ganador(secuencia3_5)

    secuencia4 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
    ]
    String4 = ganador(secuencia4)

    secuencia5 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 1, ' '],
    ]
    String5 = ganador(secuencia5)

    secuencia6 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 1, ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', 1],
    ]
    String6 = ganador(secuencia6)

    secuencia7 = [
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 1, ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', 1],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    String7 = ganador(secuencia7)

    secuencia7_5 = [
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [1, ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    String7_5 = ganador(secuencia7_5)

    secuencia8 = [
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 1, ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    String8 = ganador(secuencia8)

    secuencia9 = [
        [' ', ' ', ' ', ' ', 1, ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' '],
        [' ', ' ', 1, ' ', ' ', ' ', ' '],
        [' ', 1, ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    String9 = ganador(secuencia9)

    assert String == 0
    assert String1 == 0
    assert String2 == 0
    assert String3 == 0
    assert String3_5 == 0
    assert String4 == 0
    assert String5 == 0
    assert String6 == 0
    assert String7 == 0
    assert String7_5 == 0
    assert String8 == 0
    assert String9 == 0
    assert String0 == 0



