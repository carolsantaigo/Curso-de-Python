# Fundamentos de Python (Funções) – Parte 2

## Funções como Objetos em Python

Em Python, **funções são objetos de primeira classe**. Isso significa que elas podem ser:

- Atribuídas a variáveis
- Passadas como argumento para outras funções
- Retornadas de outras funções
- Armazenadas em estruturas de dados (listas, dicionários, etc.)

Essa característica é extremamente poderosa e permite escrever códigos flexíveis e reutilizáveis.

---

## Atribuindo uma função a uma variável

```python
def saudacao():
    print("Olá!")

cumprimento = saudacao
cumprimento()  # Chama a função saudacao
```

---

## Passando uma função como argumento

```python
def executar(func):
    print("Executando...")
    func()

def tarefa():
    print("Tarefa realizada!")

executar(tarefa)
```

---

## Retornando uma função de outra função

```python
def criar_saudacao():
    def saudacao():
        print("Bem-vindo!")
    return saudacao

minha_funcao = criar_saudacao()
minha_funcao()
```

---

## Armazenando funções em coleções

```python
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

operacoes = {
    "+": somar,
    "-": subtrair
}

print(operacoes["+"](10, 5))  # 15
print(operacoes["-"](10, 5))  # 5
```

---

## Por que isso importa?

Tratar funções como objetos abre caminho para:

- **Callbacks**
- **Decoratorss**
- **Programas mais genéricos e reutilizáveis**

---
