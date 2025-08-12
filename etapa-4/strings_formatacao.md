# Fatiamento e Formatação de Strings em Python

## Fatiamento (Slicing)

O fatiamento permite acessar partes específicas de uma string. A sintaxe básica é `[início:fim:passo]`.

```python
texto = "Python é incrível"

# Acesso por índice
print(texto[0])     # 'P'
print(texto[-1])    # 'l' (último caractere)

# Fatiamento básico
print(texto[0:6])   # 'Python'
print(texto[7:9])   # 'é'
print(texto[10:])    # 'incrível'
print(texto[:6])     # 'Python'
print(texto[::2])    # 'Pto é icií' (pulando de 2 em 2)
print(texto[::-1])   # 'levírcni é nohtyP' (invertido)
```

## Formatação de Strings

### 1. Operador % (estilo antigo)

```python
nome = "João"
idade = 30
print("Olá, %s. Você tem %d anos." % (nome, idade))
```

### 2. Método format()

```python
# Posicional
print("{0} tem {1} anos. {0} gosta de {2}".format("Maria", 25, "Python"))

# Nomeado
print("Nome: {nome}, Idade: {idade}".format(nome="Carlos", idade=40))

# Dicionário
dados = {"nome": "Ana", "profissao": "engenheira"}
print("{0[nome]} é {0[profissao]}.".format(dados))

# Formatação de números
pi = 3.14159
print("Pi: {:.2f}".format(pi))  # 3.14
print("Número: {:05d}".format(42))  # 00042
```

### 3. f-strings (Python 3.6+)

```python
nome = "Pedro"
idade = 35
print(f"{nome} tem {idade} anos.")

# Expressões dentro de f-strings
print(f"O dobro de {idade} é {idade * 2}")

# Formatação de números
preco = 19.99
print(f"Preço: R$ {preco:.2f}")

# Alinhamento
print(f"{nome:>10}")  # alinhado à direita
print(f"{nome:<10}")  # alinhado à esquerda
print(f"{nome:^10}")  # centralizado
```

## Métodos Úteis para Formatação

```python
# Justificação
texto = "Python"
print(texto.ljust(10, '-'))  # 'Python----'
print(texto.rjust(10, '-'))  # '----Python'
print(texto.center(10, '-')) # '--Python--'

# Preenchimento com zeros
numero = "42"
print(numero.zfill(5))  # '00042'
```

## Exemplos Práticos

### 1. Máscara de CPF
```python
def formatar_cpf(cpf):
    """Formata um CPF no formato 000.000.000-00"""
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

print(formatar_cpf("12345678901"))  # 123.456.789-01
```

### 2. Tabela Formatada
```python
dados = [
    ["Produto", "Preço", "Estoque"],
    ["Caneta", 2.50, 100],
    ["Caderno", 15.90, 50],
    ["Borracha", 1.20, 200]
]

for linha in dados:
    print("{:<10} {:>8.2f} {:>8}".format(*linha))
```

## Exercícios

1. Escreva uma função que receba um número de telefone (apenas dígitos) e retorne formatado: (XX) XXXXX-XXXX.
2. Crie uma função que formate uma data no formato DD/MM/AAAA para "Dia de Mês de Ano" (ex: "15/03/2023" → "15 de Março de 2023").
3. Implemente um gerador de etiquetas que formate nomes no formato "SOBRENOME, Nome" (ex: "João da Silva" → "SILVA, João").
4. Crie uma função que formate números grandes com separadores de milhar (ex: 1000000 → "1.000.000").
5. Implemente uma função que justifique um texto em um determinado número de colunas, alinhando à esquerda, direita e centralizado.
