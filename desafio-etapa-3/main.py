from application.calculadora_use_case import executar_calculo
from interface.console_interface import mostrar_resultado

def main():
    try:
        area = float(input("Informe o tamanho da área a ser pintada (em m²): "))
        resultados = executar_calculo(area)
        mostrar_resultado(resultados)
    except ValueError:
        print("Valor inválido. Digite um número.")

if __name__ == "__main__":
    main()
