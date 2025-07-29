# Fundamentos de Python (Funções) – Parte 4

## Tipos de Parâmetros em Detalhe

Nesta seção, vamos explorar em mais profundidade os diferentes tipos de parâmetros que podem ser utilizados na definição de funções em Python. Isso inclui a forma como são passados, combinados e utilizados.

---

## Parâmetros Posição vs Nomeados

- **Posicionais**: a ordem importa.
- **Nomeados**: a ordem não importa se o nome for informado.

```python
def mensagem(texto, vezes):
    print(texto * vezes)

mensagem("Oi! ", 3)                # Posicional
mensagem(vezes=2, texto="Olá! ")   # Nomeado
```

---

## Combinação de Parâmetros

Funções podem combinar diferentes tipos de parâmetros:

```python
def exemplo(a, b=2, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

exemplo(10, 20, 30, 40, nome="Ana", ativo=True)
```

> Saída:
>
> a: 10  
> b: 20  
> args: (30, 40)  
> kwargs: {'nome': 'Ana', 'ativo': True}

---

## Argument Unpacking (`*` e `**`)

Você também pode usar `*` e `**` ao chamar uma função, para "desempacotar" valores de uma tupla ou dicionário.

```python
def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos.")

dados = ("Lucas", 28)
apresentar(*dados)  # desempacota a tupla

info = {"nome": "Carla", "idade": 32}
apresentar(**info)  # desempacota o dicionário
```

---

## Resumo Visual

| Tipo       | Sintaxe             | Exemplo ao Chamar            |
|------------|---------------------|-------------------------------|
| Posicional | `def f(a, b)`       | `f(1, 2)`                     |
| Nomeado    | `def f(a, b)`       | `f(a=1, b=2)`                 |
| Padrão     | `def f(a=5)`        | `f()` ou `f(10)`              |
| `*args`    | `def f(*args)`      | `f(1, 2, 3)`                  |
| `**kwargs` | `def f(**kwargs)`   | `f(nome="João", ativo=True)` |

---
