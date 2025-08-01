def mostrar_resultado(resultados: dict):
    latas, custo_latas = resultados["apenas_latas"]
    galoes, custo_galoes = resultados["apenas_galoes"]
    latas_mix, galoes_mix, custo_mix = resultados["mistura"]

    print(f"\n>> Situação 1: Apenas latas de 18L")
    print(f"   {latas} lata(s) - Custo: R$ {custo_latas:.2f}")

    print(f"\n>> Situação 2: Apenas galões de 3.6L")
    print(f"   {galoes} galão(ões) - Custo: R$ {custo_galoes:.2f}")

    print(f"\n>> Situação 3: Mistura de latas e galões")
    print(f"   {latas_mix} lata(s) e {galoes_mix} galão(ões) - Custo: R$ {custo_mix:.2f}")
