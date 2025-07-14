# Funções nativas

## O que são?

Funções nativas (ou embutidas) são funções que já estão disponíveis por padrão no Python. Elas podem ser usadas sem a necessidade de importação.

---

## Exemplos de funções nativas comuns

### `print()`
Exibe dados no console.
```python
print("Hello, World!")
```

### `input()`
Recebe dados do usuário.
```python
nome = input("Digite seu nome: ")
```

### `len()`
Retorna o tamanho (número de elementos) de uma string, lista, etc.
```python
nome = "Python"
print(len(nome))  # 6
```

### `type()`
Retorna o tipo de dado da variável.
```python
idade = 30
print(type(idade))  # <class 'int'>
```

### `range()`
Gera uma sequência de números.
```python
for i in range(3):
    print(i)
# Saída: 0, 1, 2
```

### `int()`, `float()`, `str()`
Convertendo tipos de dados:
```python
texto = "10"
numero = int(texto)
altura = float("1.75")
idade = 25
idade_texto = str(idade)
```

---

## Outras funções nativas úteis

- `max()`: maior valor
- `min()`: menor valor
- `sum()`: soma dos elementos
- `sorted()`: ordena uma lista

### Exemplos:
```python
valores = [10, 20, 5, 7]
print(max(valores))    # 20
print(min(valores))    # 5
print(sum(valores))    # 42
print(sorted(valores)) # [5, 7, 10, 20]
```
