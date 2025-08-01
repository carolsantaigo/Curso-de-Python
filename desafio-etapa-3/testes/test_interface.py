from interface.console_interface import mostrar_resultado

def test_mostrar_resultado(capsys):
    resultado = {
        "apenas_latas": (2, 160.0),
        "apenas_galoes": (5, 125.0),
        "mistura": (1, 2, 130.0)
    }

    mostrar_resultado(resultado)
    capturado = capsys.readouterr().out

    assert ">> Situação 1" in capturado
    assert "2 lata(s)" in capturado
    assert "5 galão(ões)" in capturado
    assert "1 lata(s) e 2 galão(ões)" in capturado
