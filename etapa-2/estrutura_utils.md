# Métodos úteis (append, pop, keys, values, items, etc.)

## O que são?

Métodos são **funções embutidas** nos tipos de dados que permitem manipular seus elementos diretamente. Cada estrutura (lista, dicionário, etc.) possui seus próprios métodos.

---

## 🔹 Listas

### `append()`
Adiciona um elemento ao final da lista.
```python
frutas = ["maçã", "banana"]
frutas.append("laranja")
```

### `pop()`
Remove e retorna o último elemento da lista.
```python
ultima = frutas.pop()
```

### `insert()`
Insere um elemento em uma posição específica.
```python
frutas.insert(1, "kiwi")
```

### `remove()`
Remove o primeiro elemento com valor igual ao informado.
```python
frutas.remove("banana")
```

### `sort()` e `reverse()`
```python
numeros = [5, 2, 9, 1]
numeros.sort()      # ordena crescente
numeros.reverse()   # inverte a ordem
```

---

## 🔹 Dicionários

### `keys()`
Retorna todas as chaves do dicionário.
```python
pessoa = {"nome": "Ana", "idade": 30}
print(pessoa.keys())  # dict_keys(['nome', 'idade'])
```

### `values()`
Retorna todos os valores do dicionário.
```python
print(pessoa.values())  # dict_values(['Ana', 30])
```

### `items()`
Retorna tuplas com pares chave:valor.
```python
print(pessoa.items())  # dict_items([('nome', 'Ana'), ('idade', 30)])
```

### `get()`
Acessa uma chave com opção de valor padrão.
```python
print(pessoa.get("email", "não informado"))
```

### `update()`
Atualiza ou adiciona chaves ao dicionário.
```python
pessoa.update({"cidade": "SP"})
```
