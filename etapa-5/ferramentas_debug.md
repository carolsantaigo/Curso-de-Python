# Ferramentas de Debug em Python

Depurar código é uma parte essencial do desenvolvimento. Python oferece várias ferramentas e técnicas para ajudar a identificar e corrigir problemas em seu código.

## 1. O Módulo `pdb` (Python Debugger)

O debugger integrado do Python permite executar o código passo a passo, inspecionar variáveis e avaliar expressões.

### Uso Básico:

```python
import pdb

def calcular_media(numeros):
    # Define um ponto de parada
    pdb.set_trace()
    
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

# Teste
calcular_media([1, 2, 3, 4, 5])
```

### Comandos do pdb:
- `n` (next): Executa a próxima linha
- `s` (step): Entra em uma função
- `c` (continue): Continua a execução até o próximo breakpoint
- `l` (list): Mostra o código ao redor da linha atual
- `p <expressão>`: Avalia e imprime uma expressão
- `q` (quit): Sai do debugger
- `h` (help): Mostra ajuda

## 2. `breakpoint()` (Python 3.7+)

Uma forma mais moderna de adicionar breakpoints:

```python
def funcao_com_problema():
    x = 42
    breakpoint()  # Equivalente a import pdb; pdb.set_trace()
    y = x / 0
    return y
```

## 3. Logging para Debug

O módulo `logging` é excelente para rastrear a execução do código:

```python
import logging

# Configuração básica
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

def processar_dados(dados):
    logging.debug(f"Iniciando processamento de {len(dados)} itens")
    
    try:
        resultado = sum(dados) / len(dados)
        logging.info(f"Média calculada: {resultado}")
        return resultado
        
    except Exception as e:
        logging.error(f"Erro ao processar dados: {e}", exc_info=True)
        raise
```

## 4. `print()` para Depuração Rápida

Às vezes, um simples `print()` é suficiente:

```python
def calcular_fatorial(n):
    print(f"[DEBUG] Calculando fatorial de {n}")
    if n == 0:
        return 1
    fat = n * calcular_fatorial(n-1)
    print(f"[DEBUG] fatorial({n}) = {fat}")
    return fat
```

## 5. `assert` para Verificações

Use `assert` para verificar condições que devem ser verdadeiras:

```python
def dividir(a, b):
    assert b != 0, "Divisão por zero não é permitida"
    return a / b
```

## 6. `traceback` para Rastreamento de Exceções

Para obter mais informações sobre exceções:

```python
import traceback

try:
    # Código que pode falhar
    resultado = 10 / 0
except Exception:
    traceback.print_exc()  # Imprime o traceback completo
    print("\nInformações detalhadas:")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(f"Tipo: {exc_type.__name__}")
    print(f"Mensagem: {exc_value}")
    print(f"Arquivo: {exc_tb.tb_frame.f_code.co_filename}")
    print(f"Linha: {exc_tb.tb_lineno}")
```

## 7. Ferramentas Externas

### 7.1. `pudb`
Um debugger baseado em interface gráfica no terminal.

```bash
pip install pudb
python -m pudb seu_script.py
```

### 7.2. `ipdb`
Uma versão do pdb com suporte a autocompletar e syntax highlighting.

```bash
pip install ipdb
```

### 7.3. `pytest` para Testes
```python
# test_exemplo.py
def test_soma():
    assert 1 + 1 == 2

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## 8. Debugging em IDEs

### 8.1. VS Code
1. Configure o arquivo `.vscode/launch.json`
2. Adicione breakpoints clicando à esquerda dos números das linhas
3. Pressione F5 para iniciar o debug

### 8.2. PyCharm
1. Clique à esquerda dos números das linhas para adicionar breakpoints
2. Clique com o botão direito no arquivo e selecione "Debug"
3. Use a barra de ferramentas de debug para controlar a execução

## 9. Dicas de Debugging

1. **Isolar o Problema**: Reduza o código ao mínimo necessário para reproduzir o erro.
2. **Verifique Valores Intermediários**: Use `print()` ou breakpoints para inspecionar variáveis.
3. **Leia as Mensagens de Erro**: Elas geralmente contêm informações valiosas.
4. **Use `type()` e `dir()`**: Para inspecionar objetos desconhecidos.
5. **Teste Pequenas Partes**: Verifique cada função individualmente.

## 10. Exemplo Prático: Debugging de um Algoritmo de Ordenação

```python
def ordenar_lista(lista):
    ""
    Ordena uma lista usando o algoritmo bubble sort.
    Retorna uma nova lista ordenada.
    """
    # breakpoint()  # Descomente para depurar
    
    # Cria uma cópia para não modificar a lista original
    arr = lista.copy()
    n = len(arr)
    
    # Contador para debug
    iteracoes = 0
    
    for i in range(n):
        # Flag para verificar se houve troca nesta iteração
        trocou = False
        
        for j in range(0, n-i-1):
            # Imprime o estado atual para debug
            print(f"Iteração {iteracoes}: {arr}")
            print(f"Comparando {arr[j]} e {arr[j+1]}")
            
            if arr[j] > arr[j+1]:
                # Troca os elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocou = True
                print(f"Trocou: {arr}")
            
            iteracoes += 1
        
        # Se não houve trocas, a lista está ordenada
        if not trocou:
            break
    
    return arr

# Teste com uma lista desordenada
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
print("Ordenando...")
ordenada = ordenar_lista(lista)
print("Lista ordenada:", ordenada)
```

## Exercícios

1. **Depure um Algoritmo de Busca**: Implemente uma busca binária com bugs e use o pdb para encontrar e corrigir os problemas.

2. **Análise de Desempenho**: Use `timeit` para medir o tempo de execução de diferentes implementações de um mesmo algoritmo.

3. **Logging para Debug**: Crie um script que simule um sistema de login com diferentes níveis de log (DEBUG, INFO, WARNING, ERROR).

4. **Testes com `pytest`**: Escreva testes unitários para uma função que calcula o IMC (Índice de Massa Corporal) e use o modo de falha do pytest para depurar.

5. **Debug Remoto**: Configure o `rpdb` para depurar um script Python rodando em um ambiente remoto.

6. **Trace de Chamadas**: Use o módulo `trace` para gerar um relatório de todas as funções chamadas durante a execução de um script.

7. **Análise Estática**: Instale e execute o `pylint` ou `flake8` em um dos seus projetos para identificar possíveis problemas no código.

Lembre-se que o debugging é uma habilidade que melhora com a prática. Quanto mais você se familiarizar com as ferramentas e técnicas, mais eficiente será na identificação e correção de problemas.
