from src.batalla import Batalla

def por_menor_coeficiente(batallas: list[Batalla]) -> list[Batalla]:
    batallas_ordenadas = sorted(batallas, key=lambda b: b.duracion/b.importancia)
    return batallas_ordenadas

def por_menor_duracion(batallas: list[Batalla]) -> list[Batalla]:
    batallas_ordenadas = sorted(batallas, key=lambda b: b.duracion)
    return batallas_ordenadas

def por_mayor_importancia(batallas: list[Batalla]) -> list[Batalla]:
    batallas_ordenadas = sorted(batallas, key=lambda b: b.importancia, reverse=True)
    return batallas_ordenadas

