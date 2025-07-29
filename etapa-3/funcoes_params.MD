# Fundamentos de Python (Funções) – Parte 3

## Parâmetros em Funções

Parâmetros são valores que uma função pode receber para realizar suas operações. Eles permitem tornar a função mais genérica e reutilizável.

Em Python, existem diferentes formas de trabalhar com parâmetros:

- **Parâmetros posicionais**
- **Parâmetros nomeados**
- **Parâmetros com valor padrão**
- **Parâmetros variáveis**

---

## Parâmetros Posicionais

Os valores são passados na ordem em que os parâmetros foram definidos.

```python
def apresentar(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

apresentar("Ana", 30)
```

---

## Parâmetros Nomeados (Keyword Arguments)

Permitem passar os valores fora de ordem, especificando os nomes dos parâmetros:

```python
def apresentar(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

apresentar(idade=25, nome="Carlos")
```

---

## Parâmetros com Valor Padrão

Se um valor não for informado, o padrão será usado.

```python
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao()            # Olá, Visitante!
saudacao("Ricardo")   # Olá, Ricardo!
```

---

## Parâmetros Variáveis

### `*args` – múltiplos argumentos posicionais

Os valores são recebidos como uma **tupla**.

```python
def somar(*numeros):
    total = sum(numeros)
    print(f"Soma: {total}")

somar(1, 2, 3, 4)  # Soma: 10
```

### `**kwargs` – múltiplos argumentos nomeados

Os valores são recebidos como um **dicionário**.

```python
def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_info(nome="João", idade=40)
```

---

## Exemplo prático com `*args` e `**kwargs`

```python
def processar_pedido(*itens, **cliente):
    print("Itens do pedido:")
    for item in itens:
        print(f"- {item}")

    print("\nDados do cliente:")
    for chave, valor in cliente.items():
        print(f"{chave}: {valor}")

# Tupla e dicionário sendo passados diretamente
itens = ("Pizza", "Refrigerante", "Sobremesa")
dados = {"nome": "Mariana", "endereco": "Rua A, 123"}

processar_pedido(*itens, **dados)
```

> Saída:
>
> Itens do pedido:
> - Pizza
> - Refrigerante
> - Sobremesa
>
> Dados do cliente:
> nome: Mariana
> endereco: Rua A, 123

---

## Ordem dos Parâmetros

A ordem correta ao declarar parâmetros é:

1. Posição obrigatória
2. `*args`
3. Padrão (com valor default)
4. `**kwargs`

```python
def exemplo(a, *args, b=0, **kwargs):
    pass
```

---
