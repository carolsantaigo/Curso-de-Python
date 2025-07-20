# Compreensões de listas (list comprehensions)

## O que são?

Compreensões de listas são uma forma **concisa e eficiente** de criar novas listas em Python, usando uma sintaxe simples baseada em expressões e laços `for`.

---

## Sintaxe básica

```python
nova_lista = [expressao for item in iteravel]
```

Exemplo:
```python
numeros = [1, 2, 3, 4]
quadrados = [x**2 for x in numeros]
print(quadrados)  # [1, 4, 9, 16]
```

---

## Com condição (if)

```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

---

## Com if...else

```python
resultado = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print(resultado)  # ['par', 'impar', 'par', 'impar', 'par']
```

---

## Com listas de listas (aninhadas)

```python
matriz = [[1, 2], [3, 4]]
flatten = [num for linha in matriz for num in linha]
print(flatten)  # [1, 2, 3, 4]
```

---

## Comparando com laço tradicional

```python
# Forma tradicional
quadrados = []
for x in range(5):
    quadrados.append(x**2)

# List comprehension
quadrados = [x**2 for x in range(5)]
```
