from domain.entities import Tinta

def test_tinta_instanciada():
    tinta = Tinta(litros=10, preco=50)
    assert tinta.litros == 10
    assert tinta.preco == 50
