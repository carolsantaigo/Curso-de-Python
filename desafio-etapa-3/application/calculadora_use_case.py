from domain.services import (
    calcular_litros_com_margem,
    calcular_apenas_latas,
    calcular_apenas_galoes,
    calcular_misto
)

from domain.entities import LATA, GALAO

def executar_calculo(area_m2: float):
    litros = calcular_litros_com_margem(area_m2)
    latas, custo_latas = calcular_apenas_latas(litros, LATA)
    galoes, custo_galoes = calcular_apenas_galoes(litros, GALAO)
    latas_mix, galoes_mix, custo_mix = calcular_misto(litros, LATA, GALAO)

    return {
        "apenas_latas": (latas, custo_latas),
        "apenas_galoes": (galoes, custo_galoes),
        "mistura": (latas_mix, galoes_mix, custo_mix)
    }
