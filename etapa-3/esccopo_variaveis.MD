# Fundamentos de Python (Funções) – Parte 6

## Escopo de Variáveis

Escopo é o contexto onde uma variável pode ser acessada. Em Python, isso se divide principalmente em:

- **Escopo Local** (dentro da função)
- **Escopo Global** (fora da função)

Entender escopo é fundamental para evitar conflitos, erros e comportamentos inesperados no código.

---

## Escopo Local

Variáveis definidas dentro de uma função só existem ali.

```python
def saudacao():
    nome = "Lucas"
    print(f"Olá, {nome}!")

saudacao()
# print(nome)  # Erro: nome não está definido fora da função
```

---

## Escopo Global

Variáveis fora da função podem ser lidas dentro dela.

```python
mensagem = "Bem-vindo!"

def mostrar():
    print(mensagem)

mostrar()  # Bem-vindo!
```

---

## Modificando variável global (com `global`)

Para alterar uma variável global dentro de uma função, use a palavra-chave `global`:

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
```

Usar `global` com frequência pode dificultar a manutenção. Prefira retornar valores e reatribuir fora da função.

---

## Variáveis com mesmo nome

Se uma variável local tiver o mesmo nome da global, a local prevalece dentro da função:

```python
nome = "Julia"

def exibir():
    nome = "Carla"
    print(nome)

exibir()        # Carla
print(nome)     # Julia
```

---

## Funções aninhadas e `nonlocal`

Quando uma função está dentro de outra, o uso de `nonlocal` permite acessar variáveis da função externa:

```python
def externa():
    valor = 10

    def interna():
        nonlocal valor
        valor += 5

    interna()
    print(valor)

externa()  # 15
```

---

## Resumo

| Tipo      | Onde é declarada       | Onde pode ser usada         |
|-----------|-------------------------|------------------------------|
| Local     | Dentro de uma função    | Apenas dentro da função     |
| Global    | Fora de qualquer função | Em qualquer parte do código |
| Nonlocal  | Em função aninhada      | Dentro da função interna    |

---
