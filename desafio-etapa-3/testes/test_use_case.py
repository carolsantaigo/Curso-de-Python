from application.calculadora_use_case import executar_calculo

def test_executar_calculo():
    resultado = executar_calculo(60)  # deve dar ~11 litros

    assert resultado["apenas_latas"][0] == 1 or resultado["apenas_latas"][0] == 2
    assert resultado["apenas_galoes"][0] > 0
    assert resultado["mistura"][0] >= 0
    assert resultado["mistura"][1] >= 0
