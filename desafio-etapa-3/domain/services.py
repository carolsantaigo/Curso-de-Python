import math

def calcular_litros_com_margem(area_m2: float, rendimento_por_litro: float = 6, margem: float = 0.1) -> float:
    return (area_m2 / rendimento_por_litro) * (1 + margem)

def calcular_apenas_latas(litros: float, lata) -> tuple[int, float]:
    qtd = math.ceil(litros / lata.litros)
    return qtd, qtd * lata.preco

def calcular_apenas_galoes(litros: float, galao) -> tuple[int, float]:
    qtd = math.ceil(litros / galao.litros)
    return qtd, qtd * galao.preco

def calcular_misto(litros: float, lata, galao) -> tuple[int, int, float]:
    qtd_lata = int(litros // lata.litros)
    resto = litros - (qtd_lata * lata.litros)
    qtd_galao = math.ceil(resto / galao.litros)
    custo = (qtd_lata * lata.preco) + (qtd_galao * galao.preco)
    return qtd_lata, qtd_galao, custo
