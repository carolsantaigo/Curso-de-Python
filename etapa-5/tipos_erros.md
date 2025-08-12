# Tipos Comuns de Erros em Python

Entender os diferentes tipos de erros em Python é essencial para escrever código robusto e saber como depurá-lo. Este guia aborda os principais tipos de erros que você encontrará ao programar em Python.

## 1. Erros de Sintaxe (SyntaxError)

Ocorrem quando o código não segue a sintaxe correta da linguagem. São detectados pelo interpretador antes da execução do programa.

### Exemplos Comuns:

```python
# Falta de dois pontos
if True
    print("Olá")
# SyntaxError: expected ':'

# Parênteses desbalanceados
print("Olá"
# SyntaxError: unexpected EOF while parsing

# Uso incorreto de palavras-chave
break = 10
# SyntaxError: invalid syntax
```

### Como Corrigir:
- Verifique a mensagem de erro e a linha indicada
- Confira se todos os parênteses, colchetes e chaves estão balanceados
- Verifique se não está usando palavras reservadas como nomes de variáveis

## 2. Erros em Tempo de Execução (Exceções)

### 2.1 NameError
Ocorre quando uma variável ou nome não está definido.

```python
print(nome_nao_definido)
# NameError: name 'nome_nao_definido' is not defined
```

### 2.2 TypeError
Ocorre quando uma operação é aplicada a um objeto de tipo inadequado.

```python
# Somando tipos incompatíveis
resultado = "5" + 3
# TypeError: can only concatenate str (not "int") to str
```

### 2.3 ValueError
Ocorre quando uma função recebe um argumento com o tipo correto, mas valor inapropriado.

```python
int("abc")
# ValueError: invalid literal for int() with base 10: 'abc'
```

### 2.4 IndexError
Ocorre quando se tenta acessar um índice que não existe em uma sequência.

```python
lista = [1, 2, 3]
print(lista[5])
# IndexError: list index out of range
```

### 2.5 KeyError
Ocorre quando se tenta acessar uma chave que não existe em um dicionário.

```python
dados = {"nome": "João"}
print(dados["idade"])
# KeyError: 'idade'
```

### 2.6 AttributeError
Ocorre quando se tenta acessar um atributo ou método que não existe em um objeto.

```python
lista = [1, 2, 3]
print(lista.upper())
# AttributeError: 'list' object has no attribute 'upper'
```

### 2.7 FileNotFoundError
Ocorre quando se tenta abrir um arquivo que não existe.

```python
with open("arquivo_inexistente.txt") as f:
    conteudo = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'arquivo_inexistente.txt'
```

### 2.8 ZeroDivisionError
Ocorre quando se tenta dividir por zero.

```python
resultado = 10 / 0
# ZeroDivisionError: division by zero
```

## 3. Erros de Semântica (Lógicos)

São erros em que o código é executado sem gerar exceções, mas produz resultados incorretos.

### Exemplo:
```python
def calcular_media(numeros):
    # Erro: está usando len(numeros) - 1 em vez de apenas len(numeros)
    return sum(numeros) / (len(numeros) - 1)

# A função funciona, mas dá resultados incorretos
print(calcular_media([10, 20, 30]))  # Retorna 30 em vez de 20
```

## 4. Erros de Recursão Infinita

Ocorrem quando uma função chama a si mesma repetidamente sem uma condição de parada.

```python
def contagem_regressiva(n):
    print(n)
    contagem_regressiva(n - 1)  # Sem condição de parada

contagem_regressiva(5)  # Eventualmente causa RecursionError
```

## 5. Erros de Módulos e Importação

### 5.1 ModuleNotFoundError
Ocorre quando o módulo não é encontrado.

```python
import modulo_inexistente
# ModuleNotFoundError: No module named 'modulo_inexistente'
```

### 5.2 ImportError
Ocorre quando há um problema ao importar um módulo ou nome específico.

```python
from math import funcao_inexistente
# ImportError: cannot import name 'funcao_inexistente' from 'math'
```

## 6. Erros de Sistema Operacional

### 6.1 PermissionError
Ocorre quando não há permissão para acessar um recurso.

```python
with open("/etc/shadow") as f:
    print(f.read())
# PermissionError: [Errno 13] Permission denied: '/etc/shadow'
```

### 6.2 FileExistsError
Ocorre ao tentar criar um arquivo ou diretório que já existe.

```python
os.mkdir("diretorio_existente")
# FileExistsError: [Errno 17] File exists: 'diretorio_existente'
```

## 7. Erros de Memória

### 7.1 MemoryError
Ocorre quando uma operação esgota a memória disponível.

```python
dados = " " * (10**10)  # Tenta alocar muita memória
# MemoryError: Unable to allocate array with shape (10000000000,) and data type int64
```

## 8. Erros de Tempo de Execução (RuntimeError)

Erros que não se encaixam em outras categorias.

```python
def funcao_recursiva():
    funcao_recursiva()

funcao_recursiva()
# RecursionError: maximum recursion depth exceeded
```

## Como Lidar com Erros

1. **Leia a mensagem de erro**: A mensagem geralmente indica o tipo de erro e a linha onde ocorreu.
2. **Verifique a documentação**: Consulte a documentação da função ou método que está causando o erro.
3. **Use print() para depuração**: Adicione instruções print() para verificar valores de variáveis.
4. **Use um depurador**: Ferramentas como pdb ou o depurador integrado da sua IDE podem ajudar a identificar problemas.
5. **Pesquise na internet**: Muitos erros comuns já foram resolvidos por outras pessoas.

## Exercícios Práticos

1. Escreva um código que gere um `NameError` e depois o corrija.
2. Crie uma função que receba uma lista e um índice, e trate o `IndexError` caso o índice seja inválido.
3. Implemente um validador de entrada que evite `ValueError` ao converter strings para números.
4. Escreva um gerenciador de contexto que trate automaticamente `FileNotFoundError` ao abrir arquivos.
5. Crie um programa que simule uma calculadora com tratamento adequado para `ZeroDivisionError`.
