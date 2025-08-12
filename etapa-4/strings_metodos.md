# Métodos de String em Python

Strings em Python possuem uma variedade de métodos úteis para manipulação de texto. Aqui estão os principais:

## Métodos Básicos

```python
# Convertendo caixa
texto = "Olá Mundo"
print(texto.upper())      # 'OLÁ MUNDO'
print(texto.lower())      # 'olá mundo'
print(texto.title())      # 'Olá Mundo'
print(texto.capitalize()) # 'Olá mundo'
print(texto.swapcase())   # 'oLÁ mUNDO'

# Verificações
print(texto.islower())    # False
print(texto.isupper())    # False
print(texto.istitle())    # True
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True
print("   ".isspace())    # True
```

## Busca e Substituição

```python
# Busca
texto = "Python é incrível"
print(texto.find("incrível"))  # 10
print(texto.index("é"))        # 7
print("Python" in texto)       # True

# Contagem e substituição
print(texto.count("n"))        # 2
print(texto.replace("incrível", "fantástico"))
```

## Divisão e Junção

```python
# Dividindo strings
frutas = "maçã,banana,laranja"
lista_frutas = frutas.split(",")
print(lista_frutas)  # ['maçã', 'banana', 'laranja']

# Juntando strings
frutas_juntas = " e ".join(lista_frutas)
print(frutas_juntas)  # 'maçã e banana e laranja'
```

## Remoção de Espaços

```python
texto = "   olá   "
print(texto.strip())    # 'olá'
print(texto.lstrip())   # 'olá   '
print(texto.rstrip())   # '   olá'
```

## Formatação

```python
# Método format()
nome = "Maria"
idade = 25
print("Olá, {}. Você tem {} anos.".format(nome, idade))

# f-strings (Python 3.6+)
print(f"Olá, {nome}. Você tem {idade} anos.")

# Alinhamento
print("{:<10}".format("esquerda"))  # alinhado à esquerda
print("{:>10}".format("direita"))   # alinhado à direita
print("{:^10}".format("centro"))    # centralizado
```

## Exercícios Práticos

1. Crie uma função que conte quantas vezes uma letra aparece em uma string, ignorando maiúsculas e minúsculas.
2. Escreva um programa que receba uma frase e retorne a mesma frase com as palavras em ordem alfabética.
3. Crie uma função que remova todos os caracteres especiais de uma string, mantendo apenas letras, números e espaços.
4. Implemente um validador de e-mail simples usando métodos de string.
5. Crie um gerador de nome de usuário que pegue o primeiro nome e o sobrenome de uma string e retorne em formato de usuário (ex: "João Silva" -> "joao.silva").
