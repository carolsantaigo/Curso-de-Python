# Iteração com for e enumerate

## O que é iteração?

Iterar significa **percorrer uma sequência** (como uma lista, string ou tupla) elemento por elemento. Em Python, o laço `for` é a maneira mais comum de fazer isso.

---

## Usando `for` para iterar

```python
nomes = ["Ana", "Carlos", "Bruna"]

for nome in nomes:
    print(nome)
```

---

## Usando `enumerate()`

A função `enumerate()` permite iterar sobre os elementos **e** acessar os índices ao mesmo tempo.

```python
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")
```

---

## Exemplo com string

```python
palavra = "Python"

for letra in palavra:
    print(letra)
```

---

## Exemplo com range

```python
for i in range(5):
    print("Repetição", i)
```

---

## Comparando for vs enumerate

```python
frutas = ["maçã", "banana", "uva"]

# Sem enumerate
for i in range(len(frutas)):
    print(i, frutas[i])

# Com enumerate (mais legível)
for i, fruta in enumerate(frutas):
    print(i, fruta)
```
