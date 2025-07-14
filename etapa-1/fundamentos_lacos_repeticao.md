# Estruturas de repetição

## O que são?

Estruturas de repetição permitem que um bloco de código seja executado **múltiplas vezes** de forma automática. Em Python, utilizamos `for` e `while` para criar laços de repetição.

---

## Repetição com `for`

O `for` é usado para percorrer **sequências** como listas, strings ou intervalos de números (`range`).

### Exemplo com `range()`
```python
for i in range(5):
    print("Repetição:", i)
```

### Exemplo com lista
```python
nomes = ["Ana", "Carlos", "Bruna"]

for nome in nomes:
    print("Nome:", nome)
```

---

## Repetição com `while`

O `while` executa um bloco **enquanto** a condição for verdadeira.

### Exemplo:
```python
contador = 0

while contador < 3:
    print("Contando:", contador)
    contador += 1
```

---

## Diferenças principais

| Característica | `for` | `while` |
|------------------|-------|---------|
| Baseado em       | Sequência / range | Condição |
| Uso comum        | Quando se sabe o número de repetições | Quando não se sabe |

---

## Comandos úteis

- `break`: interrompe o laço
- `continue`: pula para a próxima iteração

### Exemplo com `break`:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Exemplo com `continue`:
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```