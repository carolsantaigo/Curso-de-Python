# Fundamentos de Python (Funções) – Parte 5

## A Instrução `return`

A palavra-chave `return` é usada em funções para devolver um valor para quem chamou aquela função. Ao ser executado, o `return` encerra imediatamente a função e envia o valor indicado.

---

## Retornando um valor simples

```python
def quadrado(n):
    return n * n

resultado = quadrado(5)
print(resultado)  # 25
```

---

## `return` encerra a função

Qualquer código após o `return` não será executado:

```python
def exemplo():
    return "fim"
    print("isso nunca será impresso")
```

---

## Retornando múltiplos valores

É possível retornar vários valores separando-os por vírgula. O Python empacota os valores como uma tupla.

```python
def coordenadas():
    x = 10
    y = 20
    return x, y

ponto = coordenadas()
print(ponto)        # (10, 20)
print(ponto[0])     # 10
```

---

## Retorno condicional

O `return` pode ser usado dentro de estruturas de controle para devolver valores diferentes conforme a lógica:

```python
def classificar(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
```

---

## `return` vs `print`

- `print()` apenas exibe um valor na tela.
- `return` devolve um valor que pode ser armazenado, manipulado ou passado adiante.

```python
def saudacao():
    return "Olá!"

texto = saudacao()
print(texto)  # Olá!
```

---

## Retornando `None`

Se não houver `return`, ou se ele for usado sozinho, a função retorna `None`:

```python
def nada():
    pass

print(nada())  # None
```
