from dataclasses import dataclass

@dataclass
class Tinta:
    litros: float
    preco: float

LATA = Tinta(litros=18, preco=80.0)
GALAO = Tinta(litros=3.6, preco=25.0)
