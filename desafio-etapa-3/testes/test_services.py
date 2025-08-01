from domain.services import (
    calcular_litros_com_margem,
    calcular_apenas_latas,
    calcular_apenas_galoes,
    calcular_misto
)
from domain.entities import Tinta

LATA = Tinta(litros=18, preco=80.0)
GALAO = Tinta(litros=3.6, preco=25.0)

def test_calcular_litros_com_margem():
    litros = calcular_litros_com_margem(60)
    assert round(litros, 2) == 11.0

def test_calcular_apenas_latas():
    qtd, custo = calcular_apenas_latas(54, LATA)
    assert qtd == 3
    assert custo == 240.0

def test_calcular_apenas_galoes():
    qtd, custo = calcular_apenas_galoes(10, GALAO)
    assert qtd == 3
    assert custo == 75.0

def test_calcular_misto():
    latas, galoes, custo = calcular_misto(50, LATA, GALAO)
    assert latas == 2
    assert galoes == 4
    assert custo == (2 * 80.0 + 4 * 25.0)
